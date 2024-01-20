import copy
from typing import Any, Mapping, Sequence, Callable

from uniflow.node import Node
from uniflow.op.op import Op

class ExpandOp(Op):
    """Expand operation class."""
    
    def __init__(self, name: str = None, expand_func: Callable[[int, Any], int] = None):
        """Initialize ExpandOp.
        
        Args:
            name (str): (Optional) Name of the operation.
        """
        super().__init__(name=name)
        if expand_func:
            self._expand_func = expand_func
        else:
            self._expand_func = lambda index, node: index < len(node.value_dict) // 2 # default expand_func


    def __call__(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Expand operation.
        
        Args:
            nodes (Sequence[Node]): Input nodes.
            expand_func (Callable[[int, Any], int]): (Optional) Input function that specifies how node should be split.
            
        Returns:
            Sequence[Node]: Output nodes.
        """
           
        output_nodes = []     
        
        for node in nodes:
            dict1, dict2 = dict(), dict()
            value_dict = node.value_dict if type(node.value_dict) == dict else node.value_dict[0]
            for index, key in enumerate(value_dict.keys()):
                if self._expand_func(index, node):
                    dict1[key] = copy.deepcopy(value_dict[key])
                else:
                    dict2[key] = copy.deepcopy(value_dict[key])
            output_node = [
                Node(name=self.unique_name(), value_dict=dict1, prev_nodes=[node]),
                Node(name=self.unique_name(), value_dict=dict2, prev_nodes=[node]),
            ]
            output_nodes.extend(output_node)
        return output_nodes
    