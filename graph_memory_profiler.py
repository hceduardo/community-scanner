"""Provides means to measure graph size in memory in terms of number of edges"""

from inout.parser import parse, get_headers
import config as cfg
import os
from memory_profiler import memory_usage
from time import time
import sys

__author__ = "Eduardo Hernandez"
__email__ = "https://www.linkedin.com/in/eduardohernandezj/"

DEFAULT_EDGES_FILE = os.path.join(cfg.BASE_DIR, "sample_files", "girvan_graph.csv")


def main():

    edges_path = DEFAULT_EDGES_FILE if len(sys.argv) < 2 else sys.argv[1]

    source_header, target_header, weight_header = get_headers(edges_path)

    before_memory = memory_usage()[0]
    before_time = time()

    graph = parse(edges_path,
                  source_header=source_header, target_header=target_header, weight_header=weight_header,
                  edge_limit=cfg.EDGES_LIMIT)

    elapsed_time = time() - before_time
    consumed_memory = memory_usage()[0] - before_memory

    print('Number of edges: {0:,}, Graph Size in Memory (MB): {1:5.2f}, Parsing Time (seconds): {2:10.2}'.format(
        cfg.EDGES_LIMIT, consumed_memory, elapsed_time
    ))

    del graph


if __name__ == '__main__':
    main()


