# from btp.behavior_tree.scene.scene import Scene
# from btp.behavior_tree.behavior_tree.btml.btmlCompiler import load

import os
from btp.utils.path import get_root_path
from btp.bt.utils.draw import render_dot_tree
from btp.bt.utils.load import load_bt_from_btml

if __name__ == '__main__':

    # create robot
    root_path = get_root_path()
    btml_path = os.path.join(root_path, 'btp.behavior_tree/utils/draw_bt/robot.bt')
    behavior_lib_path = os.path.join(root_path, 'btp.behavior_tree/behavior_lib')
    bt = load_bt_from_btml(None, btml_path, behavior_lib_path)



    render_dot_tree(bt.root,name="llm_test",png_only = False)
    # build and tick