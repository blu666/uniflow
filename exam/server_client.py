import sys

sys.path.append(".")
sys.path.append("..")
sys.path.append("../..")

from uniflow.flow.client import TransformClient
from uniflow.flow.config import TransformExpandReduceConfig
from uniflow.viz import Viz

client = TransformClient(TransformExpandReduceConfig())
input = [{"How are you?": "Fine.", "Who are you?": "I am Bob."}, {"Where are you?": "I am at home.", "What are you doing?": "Coding."}]
output = client.run(input)

print(output)

graph = Viz.to_digraph(output[1]['root'])
graph.view()