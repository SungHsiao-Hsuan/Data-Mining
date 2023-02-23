from pathlib import Path
from typing import List
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

import args
import config
import utils

import my_algos
from collections import defaultdict

def main():
    # Parse command line arguments
    a = args.parse_args()

    input_data: List[List[str]] = utils.read_file(config.IN_DIR / a.dataset)
    filename = Path(a.dataset).stem

    # Create graph
    graph = generate_total_nodes(input_data)

    # Calculate HITS then Export authority and hub output file
    start = time.time()
    authority, hubs = my_algos.HITS(graph, 30, 1e-06)
    result_HITS = time.time() - start
    print(f"HITS executed time: {result_HITS}")

    # Write authority
    utils.write_file(
        data = authority,
        filename = config.OUT_DIR / a.authority
    )

    # Write hubs
    utils.write_file(
        data = hubs,
        filename = config.OUT_DIR / a.hub
    )

    # Calculate PageRank and Export PageRank output file
    start = time.time()
    page_rank  = my_algos.PageRank(graph,0.1,30)
    result_PageRank = time.time() - start
    print(f"PageRank executed time: {result_PageRank}")


    utils.write_file(
        data = page_rank,
        filename = config.OUT_DIR / a.PageRank
    )

    # Calculate SimRank and Export SimRank output file
    start = time.time()
    simRank = my_algos.SimRank(graph,0.7,30)
    result_SimRank = time.time() - start
    print(f"SimRank executed time: {result_SimRank}")

    np.savetxt(config.OUT_DIR / a.SimRank, simRank, fmt='%.3f', delimiter=' ')


# Create graph
def generate_total_nodes(dataset):

    total_transaction = defaultdict(set)

    for i, j in dataset:
        total_transaction[i].add(j)

    return total_transaction


if __name__ == "__main__":
    main()