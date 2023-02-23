import networkx as nx
import matplotlib.pyplot as plt

import config
from args import *
import utils

from typing import List

import matplotlib.pyplot as plt

input_data: List[List[str]] = utils.read_file(config.IN_DIR / f"{title}.txt")


G = nx.DiGraph()
G.add_edges_from(input_data)
nx.draw(G,with_labels = True)
plt.show()




