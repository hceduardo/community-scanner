"""Module to parse Graph objects from csv sample_files"""

import csv
import os
from model.graph import Graph

__author__ = "Eduardo Hernandez"
__email__ = "https://www.linkedin.com/in/eduardohernandezj/"


def parse(edges_path, source_header='source', target_header='target', weight_header='weight',
          edge_limit=None) -> Graph:
    """
    Parse graph from input file
    :param edges_path: input file
    :param source_header: header for source node
    :param target_header: header for target node
    :param weight_header: header for weight
    :param edge_limit: limit the number of edges to parse from file
    :return: Graph object
    """
    # ToDo: parse by streaming to avoid loading a large graph to memmory
    # ToDo: parse nodes and edges properties
    # ToDo: validate inputs

    name = get_name_from_path(edges_path)
    edges = list()

    with open(edges_path, mode='r') as edges_file:
        edges_reader = csv.DictReader(edges_file, delimiter=',')
        for i, row in enumerate(edges_reader):

            if edge_limit is not None and i >= edge_limit:
                break

            edges.append((
                int(row[source_header]),
                int(row[target_header]),
                float(row[weight_header])
            ))

    graph = Graph(name)
    graph.add_edges(edges)
    return graph


def get_name_from_path(edges_path):
    return os.path.basename(edges_path).split(".")[0]


def get_headers(edges_path):
    with open(edges_path, mode='r') as edges_file:
        first_line = edges_file.readline().rstrip()

    return first_line.split(',')