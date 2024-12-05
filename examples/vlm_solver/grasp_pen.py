import os
import yaml
import omnigibson as og
from omnigibson.macros import gm
import omnigibson.utils.transform_utils as T
import torch as th
import math
import random
import time
import numpy as np
from btgym import ROOT_PATH
from btgym.core.curobo import CuRoboMotionGenerator
from btgym.utils.og_utils import OGCamera
import sys
import importlib.util
import importlib
from omnigibson.action_primitives.starter_semantic_action_primitives import (
    StarterSemanticActionPrimitives,
    StarterSemanticActionPrimitiveSet,
)
from btgym.utils.logger import log,set_logger_entry
from btgym.utils import cfg
import cv2

th.set_printoptions(precision=4)
code_path = os.path.join(ROOT_PATH, "../examples/vlm_solver/cached")
sys.path.append(code_path)

def execute_controller(ctrl_gen, env):
    for action in ctrl_gen:
        # print(f"action: {action}")
        env.step(action)


class ObjInEnv:
    def __init__(self, env, obj_name):
        self.env = env
        self.obj_name = obj_name

    def get_bbox(self):
        obj = self.env.scene.get_object(self.obj_name)
        return obj.get_base_aligned_bbox(visual=False)



class Env:
    def __init__(self):
        # 加载配置文件
        config_filename = os.path.join(ROOT_PATH, "assets/fetch_primitives.yaml")
        self.config = yaml.load(open(config_filename, "r"), Loader=yaml.FullLoader)
        self.config["scene"]["scene_file"] = os.path.join(ROOT_PATH, "assets/og_scene_file_red_pen.json")
        self.output_dir = os.path.join(cfg.OUTPUTS_PATH, "grasp_pen")
        os.makedirs(self.output_dir, exist_ok=True)

        # 初始化环境
        self.og_env = og.Environment(configs=self.config)
        self.scene = self.og_env.scene
        self.robot = self.og_env.robots[0]
        self.robot.reset()
        # 启用相机控制
        og.sim.enable_viewer_camera_teleoperation()
        self._initialize_cameras(self.config['camera'])
        self.gripper_open = True
        # 初始化运动规划器
        self.curobo_mg = CuRoboMotionGenerator(
            self.robot,
            robot_cfg_path=os.path.join(ROOT_PATH, "assets/fetch_description_curobo.yaml"),
            debug=False
        )
        
        # 设置夹爪初始位置
        self.curobo_mg.mg.kinematics.lock_joints = {
            "r_gripper_finger_joint": 0.0,
            "l_gripper_finger_joint": 0.0
        }

        # from omni.isaac.core.objects import cuboid
        # # 创建可视化目标点
        # self.visual_cube = cuboid.VisualCuboid(
        #     "/World/visual",
        #     position=np.array([-0.13, 0, 0.96]),
        #     orientation=np.array([0, 1, 0, 0]),
        #     color=np.array([1.0, 0, 0]),
        #     size=0.05,
        # )
        self.action_primitive = StarterSemanticActionPrimitives(self.og_env,enable_head_tracking=False)

        self.obj_name_map = {
            "pen_1": "Pen",
            "pencil_holder_1": "PencilHolder"
        }

        for _ in range(10):
            og.sim.step()

        self.save_images()    

    def idle(self):
        while True:
            og.sim.step()

    def reset(self):
        self.og_env.reset()
        self.robot.reset()

    def _initialize_cameras(self, cam_config):
        """
        ::param poses: list of tuples of (position, orientation) of the cameras
        """
        self.cams = dict()
        for cam_id in cam_config:
            cam_id = int(cam_id)
            self.cams[cam_id] = OGCamera(self.og_env, cam_config[cam_id])
        for _ in range(10): 
            og.sim.render()

    def get_grasp_poses_for_object_sticky(self, target_obj):
        """获取物体的抓取姿态"""
        bbox_center_in_world, bbox_quat_in_world, bbox_extent_in_base_frame, _ = target_obj.get_base_aligned_bbox(
            visual=False
        )

        grasp_center_pos = bbox_center_in_world
        # grasp_center_pos = bbox_center_in_world + th.tensor([0, 0, th.max(bbox_extent_in_base_frame) + 0.05])
        towards_object_in_world_frame = bbox_center_in_world - grasp_center_pos
        towards_object_in_world_frame /= th.norm(towards_object_in_world_frame)

        grasp_quat = T.euler2quat(th.tensor([0, math.pi / 2, 0], dtype=th.float32))
        grasp_pose = (grasp_center_pos, grasp_quat)
        
        return [(grasp_pose, towards_object_in_world_frame)]

        
    def gripper_control(self, open=True):
        joint_positions = self.robot.get_joint_positions()
        action = th.zeros(self.robot.n_joints)
        action[4] = joint_positions[2]
        action[5] = joint_positions[4]
        action[6:-2] = joint_positions[6:-2]
        gripper_target = 0.05 if open else 0.0
        action[-2:] = gripper_target
        for _ in range(20):
            self.og_env.step(action.to('cpu'))
        self.gripper_open = open

        for _ in range(20):
            og.sim.step()

    def open_gripper(self):
        self.gripper_control(open=True)


    def close_gripper(self):
        self.gripper_control(open=False)


    def reach_pose(self, pose):
        """到达指定位姿"""
        pos, euler = pose
        euler = euler * math.pi / 180
        quat = T.euler2quat(euler)

        # 检查并调整关节位置
        jp = self.robot.get_joint_positions(normalized=True)
        if not th.all(th.abs(jp)[:-2] < 0.97):
            new_jp = jp.clone()
            new_jp[:-2] = th.clamp(new_jp[:-2], min=-0.95, max=0.95)
            self.robot.set_joint_positions(new_jp, normalized=True)
        og.sim.step()

        pos_sequence = th.stack([pos, pos])
        quat_sequence = th.stack([quat, quat])
        obj_in_hand = self.action_primitive._get_obj_in_hand()
        log(f"obj_in_hand: {obj_in_hand}")
        successes, paths = self.curobo_mg.compute_trajectories(pos_sequence, quat_sequence, attached_obj=obj_in_hand)
        if successes[0]:
            self.execute_trajectory(paths[0])

        for _ in range(50):
            og.sim.step()



    def execute_trajectory(self, path):
        """执行轨迹"""
        joint_trajectory = self.curobo_mg.path_to_joint_trajectory(path)
        current_joint_positions = self.robot.get_joint_positions()
        for time_i, joint_positions in enumerate(joint_trajectory):
            full_action = th.zeros(self.robot.n_joints, device=joint_positions.device)
            full_action[4:-2] = joint_positions[:-2]
            if self.gripper_open:
                full_action[-2:] = 0.05
            else:
                full_action[-2:] = 0.0
            self.og_env.step(full_action.to('cpu'))

    # def follow_cube(self):
    #     """运行主循环"""
    #     n = 0
    #     while True:
    #         cube_position, cube_orientation = self.visual_cube.get_world_pose()
    #         try:
    #             self.reach_pose(th.tensor(cube_position), th.tensor(cube_orientation))
    #         except Exception as e:
    #             n += 1
    #             if n > 10:
    #                 self.reset_robot()
    #                 n = 0
    #             print(f"Error: {e}")
    #         og.sim.step()

    def get_cam_obs(self):
        self.last_cam_obs = dict()
        for cam_id in self.cams:
            self.last_cam_obs[cam_id] = self.cams[cam_id].get_obs()  # each containing rgb, depth, points, seg
        return self.last_cam_obs
    

    def save_images(self):
        """保存所有相机图像"""
        cam_obs = self.get_cam_obs()
        
        # 遍历每个相机
        for cam_id, obs in cam_obs.items():
            # 保存RGB图像
            rgb = obs['rgb']
            if rgb is not None:
                rgb_path = os.path.join(self.output_dir, f'camera_{cam_id}_rgb.png')
                # 确保rgb是numpy数组并且是uint8类型
                if not isinstance(rgb, np.ndarray):
                    rgb = np.array(rgb)
                if rgb.dtype != np.uint8:
                    rgb = (rgb * 255).astype(np.uint8)
                # RGB转BGR
                bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
                cv2.imwrite(rgb_path, bgr)
                
            # 保存深度图像
            if 'depth' in obs and obs['depth'] is not None:
                depth = obs['depth']
                if not isinstance(depth, np.ndarray):
                    depth = np.array(depth)
                # 将深度图归一化到0-255范围
                depth_normalized = ((depth - depth.min()) / (depth.max() - depth.min()) * 255).astype(np.uint8)
                depth_path = os.path.join(self.output_dir, f'camera_{cam_id}_depth.png')
                cv2.imwrite(depth_path, depth_normalized)
                
            # 保存分割图像
            if 'seg_instance' in obs and obs['seg_instance'] is not None:
                seg_instance = obs['seg_instance']

                # TODO：1. seg_instance给每个像素分配了实例id，但还不知道每个id对应哪些物体，需要根据id获取物体
                # TODO：2. 如何得到感兴趣的物体，并针对性的在物体上画格子？对于大小不同的物体，格子大小也不同吗？

                if not isinstance(seg_instance, np.ndarray):
                    seg_instance = np.array(seg_instance.cpu())
                if seg_instance.dtype != np.uint8:
                    seg_instance = seg_instance.astype(np.uint8)
                seg_path = os.path.join(self.output_dir, f'camera_{cam_id}_seg.png')
                cv2.imwrite(seg_path, seg_instance)

            
            # 获取seg中的唯一值
            # unique_values = np.unique(seg_instance)
            # log(f"unique_values: {unique_values}")
            
            # # 遍历每个uid并获取对应的物体
            # for uid in unique_values:
            #     log(f"uid: {uid}")
            #     obj = self.get_obj_by_uid(uid)
            #     if obj is not None:
            #         log(f"Found object with uid {uid}: {obj.name}")
            #     else:
            #         log(f"No object found with uid {uid}")

            # # 保存点云图像
            # if 'points' in obs and obs['points'] is not None:
            #     points = obs['points']
            #     if not isinstance(points, np.ndarray):
            #         points = np.array(points)
            #     points_path = os.path.join(self.output_dir, f'camera_{cam_id}_points.npy')
            #     np.save(points_path, points)
                
        print(f"图像已保存到目录: {self.output_dir}")

    def get_obj_by_uid(self, uid):
        """通过uid获取场景中的物体对象
        
        Args:
            uid (int): 物体的唯一标识符
            
        Returns:
            Object: OmniGibson物体对象，如果未找到则返回None
        """
        # 遍历场景中的所有物体
        for obj in self.scene.objects:
            # 获取物体的uid
            obj_uid = obj.get_body_ids()[0]  # 获取物体的body id作为uid
            if obj_uid == uid:
                return obj
        return None

    def get_obj_bbox(self, obj_name):
        obj_name = obj_name.capitalize()
        obj_cls = importlib.import_module(f"{obj_name}.{obj_name}")
        return obj_cls.get_bbox()

    def get_obj(self, obj_name):
        plan_obj_name = self.obj_name_map[obj_name]
        obj = importlib.import_module(f"{plan_obj_name}").__getattribute__(plan_obj_name)(self,self.scene.object_registry("name", obj_name))
        return obj
    
    def get_involved_object_names(self):
        return ["pen_1", "pencil_holder_1"]
    
    def do_task(self,instruction):
        """现在先不管 instruction，先写好预定义的代码，跑通执行的pipeline。想清楚我们需要什么样的代码，再考虑大模型如何生成代码"""
        pass
        # self.save_images()
        # spec = importlib.util.find_spec('task.do_task')
        # module = importlib.util.module_from_spec(spec)
        # spec.loader.exec_module(module)
        # module.do_task(self)




if __name__ == "__main__":
    set_logger_entry(__file__)

    # Env().idle()
    env = Env()
    importlib.import_module("task").do_task(env)
    env.idle()
    # env = Env()
    # print("开始任务!")
    # env.do_task("grasp the pen")
    # while True:
    #     env.grasp_obj("pen_1")

