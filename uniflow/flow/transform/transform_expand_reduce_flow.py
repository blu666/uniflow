from typing import Any, Dict, Sequence

from uniflow.constants import TRANSFORM
from uniflow.flow.flow import Flow
from uniflow.node import Node
from uniflow.op.basic.expand_op import ExpandOp
from uniflow.op.basic.reduce_op import ReduceOp
from uniflow.op.prompt import PromptTemplate

class TransformExpandReduceFlow(Flow):
    """Expand Reduce Flow."""

    TAG = TRANSFORM

    def __init__(
        self,
    ) -> None: 
        """Initialize CopyFlow class."""
        self._expand_op = ExpandOp(name="expand_op")
        self._reduce_op = ReduceOp(name="reduce_op")
        super().__init__()

    def run(self, node: Sequence[Node]) -> Sequence[Node]:
        """Run ExpandReduceFlow.

        Args:
            node (Sequence[Node]): Node to run.

        Returns:
            Sequence[Node]: Nodes after running.
        """
        expand_nodes = self._expand_op(node)
        return self._reduce_op(expand_nodes[0], expand_nodes[1])