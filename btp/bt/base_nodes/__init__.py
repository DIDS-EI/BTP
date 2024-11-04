from btp.bt.base_nodes.Action import Action
from btp.bt.base_nodes.Condition import Condition
from btp.bt.base_nodes.Inverter import Inverter
from btp.bt.base_nodes.Fallback import Fallback
from btp.bt.base_nodes.Sequence import Sequence
from btp.bt.base_nodes.CompositeAction import CompositeAction
from btp.bt.base_nodes.CompositeCondition import CompositeCondition


base_node_map = {
    "act": Action,
    "action": Action,
    "composite_action": Action,

    "cond": Condition,
    "condition": Condition,
}

base_node_type_map={
    "Action": 'Action',
    "act": 'Action',
    "action": 'Action',
    "composite_action": 'Action',
    "sub": 'Action',
    "subtree": 'Action',

    "Condition": "Condition",
    "cond": "Condition",
    "condition": "Condition",
}

control_node_map = {
    "not": Inverter,
    "selector": Fallback,
    "fallback": Fallback,
    "sequence": Sequence
}


composite_node_map = {

    "act": CompositeAction,
    "action": CompositeAction,
    "composite_action": CompositeAction,
    "sub": CompositeAction,
    "subtree": CompositeAction,


    "cond" : CompositeCondition,
    "condition" : CompositeCondition,
    "composite_condition" : CompositeCondition,
}