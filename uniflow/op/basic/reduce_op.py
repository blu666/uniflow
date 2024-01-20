import copy
from typing import Any, Mapping, Sequence, Callable

from uniflow.node import Node
from uniflow.op.op import Op


class ReduceOp(Op):
    # def __init__(self, reduce_func: Callable[[int, Any], int] = None) -> None:
    #     super().__init__()
    #     if reduce_func:
    #         self._reduce_func = reduce_func
    #     else:
    #         def reduce_func(dict1, dict2):
    #             new_value_dict = dict()
    #             len1, len2 = len(dict1), len(dict2)
    #             for index in range(max(len1, len2)):
    #                 if index >= len1:
    #                     new_value_dict[list(dict2.keys())[index]] = copy.deepcopy(list(dict2.values())[index])
    #                 elif index >= len2:
    #                     new_value_dict[list(dict1.keys())[index]] = copy.deepcopy(list(dict1.values())[index])
    #                 else:
    #                     newkey = list(dict1.keys())[index] + " " + list(dict2.keys())[index]
    #                     # value of the value_dict can be Any type, thus concatenate them into a list
    #                     newval = [copy.deepcopy(list(dict1.values())[index]), copy.deepcopy(list(dict2.values())[index])]
    #                     new_value_dict[newkey] = newval
    #             return new_value_dict
            
    #         self._reduce_func = reduce_func

    def __call__(self, node1: Sequence[Node], node2: Sequence[Node], reduce_func: Callable[[int, Any], int] = None) -> Sequence[Node]:
        """Reduce operation.

        Args:
            node1 (Sequence[Node]): Input node.
            node2 (Sequence[Node]): Input node.
            reduce_func (Callable[[int, Any], int]): (Optional) Input reduce function that specifies how nodes should be combined.

        Returns:
            Sequence[Node]: Output node.
        """

        if reduce_func:
            self._reduce_func = reduce_func
        else:
            def reduce_func(dict1, dict2):
                new_value_dict = dict()
                len1, len2 = len(dict1), len(dict2)
                for index in range(max(len1, len2)):
                    if index >= len1:
                        new_value_dict[list(dict2.keys())[index]] = copy.deepcopy(list(dict2.values())[index])
                    elif index >= len2:
                        new_value_dict[list(dict1.keys())[index]] = copy.deepcopy(list(dict1.values())[index])
                    else:
                        newkey = list(dict1.keys())[index] + " " + list(dict2.keys())[index]
                        # value of the value_dict can be Any type, thus concatenate them into a list
                        newval = [copy.deepcopy(list(dict1.values())[index]), copy.deepcopy(list(dict2.values())[index])]
                        new_value_dict[newkey] = newval
                return new_value_dict
            
            self._reduce_func = reduce_func
        new_value_dict = self._reduce_func(node1.value_dict, node2.value_dict)
        output_node = Node(name=self.unique_name(), value_dict=new_value_dict, prev_nodes=[node1, node2])
        return [output_node]
