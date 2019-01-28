"""Provides means to measure graph size in memory in terms of number of edges"""

from inout.parser import parse
import config as cfg
import os
from memory_profiler import memory_usage
from time import time

__author__ = "Eduardo Hernandez"
__email__ = "https://www.linkedin.com/in/eduardohernandezj/"


def main():
    edges_file = 'edges.csv'
    source_header, target_header, weight_header = 'V1', 'V2', 'Weight'
    edges_path = os.path.join(cfg.IN_DIR, edges_file)

    edge_limit = 100000

    before_memory = memory_usage()[0]
    before_time = time()

    graph = parse(edges_path,
                  source_header=source_header, target_header=target_header, weight_header=weight_header,
                  edge_limit=edge_limit)

    elapsed_time = time() - before_time
    consumed_memory = memory_usage()[0] - before_memory

    print('Number of edges: {0:,}, Graph Size in Memory (MB): {1:5.2f}, Parsing Time (seconds): {2:10.2}'.format(
        edge_limit, consumed_memory, elapsed_time
    ))

    del graph


if __name__ == '__main__':
    main()


