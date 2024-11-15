import os

import yaml

import omnigibson as og
from omnigibson.action_primitives.starter_semantic_action_primitives import (
    StarterSemanticActionPrimitives,
    StarterSemanticActionPrimitiveSet,
)
from omnigibson.macros import gm

# Don't use GPU dynamics and use flatcache for performance boost
# gm.USE_GPU_DYNAMICS = True
# gm.ENABLE_FLATCACHE = True

def get_config(config_path=None):
    if config_path is None:
        this_file_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(this_file_dir, 'configs/config.yaml')
    assert config_path and os.path.exists(config_path), f'config file does not exist ({config_path})'
    with open(config_path, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config


def execute_controller(ctrl_gen, env):
    for action in ctrl_gen:
        env.step(action)


def main():
    """
    Demonstrates how to use the action primitives to pick and place an object in an empty scene.

    It loads Rs_int with a robot, and the robot picks and places a bottle of cologne.
    """
    global_config = get_config(config_path="/home/admin01/workspace/OBTP/examples/config.yaml")['env']
    scene_file = '/home/admin01/workspace/OBTP/examples/og_scene_file_red_pen.json'
    global_config['scene']['scene_file'] = scene_file

        
    # Load the config
    # config_filename = os.path.join(og.example_config_path, "tiago_primitives.yaml")
    # config = yaml.load(open(config_filename, "r"), Loader=yaml.FullLoader)

    # # Update it to create a custom environment and run some actions
    # config["scene"]["scene_model"] = "Rs_int"  #restaurant_cafeteria
    # config["scene"]["load_object_categories"] = ["floors", "ceilings", "walls", "coffee_table"]
    
    # # 输出所有物体
    # for obj in scene.get_objects():
    #     print(obj.name)
    
    # 写一个物体的集合，随即从里面选择一个物体，拿起来
    # config["objects"] = [
    #     {
    #         "type": "DatasetObject",
    #         "name": "cologne",
    #         "category": "bottle_of_cologne",
    #         "model": "lyipur",
    #         "position": [-0.3, -0.8, 0.5],
    #         "orientation": [0, 0, 0, 1],
    #     },
    #     {
    #         "type": "DatasetObject",
    #         "name": "table",
    #         "category": "breakfast_table",
    #         "model": "rjgmmy",
    #         "scale": [0.3, 0.3, 0.3],
    #         "position": [-0.7, 0.5, 0.2],
    #         "orientation": [0, 0, 0, 1],
    #     },
    # ]

    # Load the environment
    # env = og.Environment(configs=config)
    # scene = env.scene
        
    env = og.Environment(dict(scene=global_config['scene'], \
        robots=[global_config['robot']['robot_config']], env=global_config['og_sim']))
    scene = env.scene
    env.scene.update_initial_state()
    robot = env.robots[0]

    # Allow user to move camera more easily
    og.sim.enable_viewer_camera_teleoperation()

    controller = StarterSemanticActionPrimitives(env, enable_head_tracking=False)

    # Grasp of cologne
    # grasp_obj = scene.object_registry("name", "cologne")
    # print("Executing controller")

    # primitive_action = controller.apply_ref(StarterSemanticActionPrimitiveSet.GRASP, grasp_obj)

    # execute_controller(primitive_action, env)
    # print("Finished executing grasp")
    
    
    # moveto
    # move_obj = scene.object_registry("name", "cologne")
    # primitive_action = controller.apply_ref(StarterSemanticActionPrimitiveSet.NAVIGATE_TO, move_obj)
    # execute_controller(primitive_action, env)
    # print("Finished executing move")
    
    # grasp
    
    

    # Place cologne on another table
    # print("Executing controller")
    # table = scene.object_registry("name", "table")
    # execute_controller(controller.apply_ref(StarterSemanticActionPrimitiveSet.PLACE_ON_TOP, table), env)
    # print("Finished executing place")


if __name__ == "__main__":
    main()
