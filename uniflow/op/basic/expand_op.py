import copy
from typing import Any, Mapping, Sequence, Callable

from uniflow.node import Node
from uniflow.op.op import Op

class ExpandOp(Op):
    # def __init__(self, expand_func: Callable[[int, Any], int] = None) -> None:
    #     super().__init__()
    #     if expand_func:
    #         self._expand_func = expand_func
    #     else:
    #         self._expand_func = lambda index, node: index > len(node.value_dict) // 2 # default expand_func
    
    def __call__(self, nodes: Sequence[Node], expand_func: Callable[[int, Any], int] = None) -> Sequence[Node]:
        """Expand operation.
        
        Args:
            nodes (Sequence[Node]): Input nodes.
            expand_func (Callable[[int, Any], int]): (Optional) Input function that specifies how node should be split.
            
        Returns:
            Sequence[Node]: Output nodes.
        """
        if expand_func:
            self._expand_func = expand_func
        else:
            self._expand_func = lambda index, node: index > len(node.value_dict) // 2 # default expand_func
        
        output_nodes = []
        for node in nodes:
            
            # print(node, flush=True)
            # print(type(node.value_dict[0]), flush=True)
            # print(len(node.value_dict), flush=True)
            dict1, dict2 = dict(), dict()
            for index, key in enumerate(node.value_dict[0].keys()):
                # print(index, key, flush=True)
                if self._expand_func(index, node):
                    dict1[key] = copy.deepcopy(node.value_dict[0][key])
                else:
                    dict2[key] = copy.deepcopy(node.value_dict[0][key])
            output_node = [
                Node(name=self.unique_name(), value_dict=dict1, prev_nodes=[node]),
                Node(name=self.unique_name(), value_dict=dict2, prev_nodes=[node]),
            ]
            output_nodes.extend(output_node)
        return output_nodes
    