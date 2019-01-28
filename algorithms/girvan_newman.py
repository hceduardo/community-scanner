"""Girvan-Newman community detection algorithm implementation"""

from algorithms.connected import connected_components
from algorithms.connected import number_connected_components
from algorithms.betweenness import get_edges_with_highest_betweenness as get_edges_with_highest_betweenness

__author__ = "Eduardo Hernandez"
__email__ = "https://www.linkedin.com/in/eduardohernandezj/"


def girvan_newman(graph, level):
    """Returns communities at certain level"""

    comp = girvan_newman_generator(graph)

    for c in comp:
        if len(c) == level:
            return c


def girvan_newman_generator(graph):
    """Generator of communities"""

    if graph.number_of_edges() == 0:
        yield tuple(connected_components(graph))
        return

    _graph = graph.copy()
    _remove_self_loops(_graph)

    while _graph.number_of_edges() > 0:
        yield _without_highest_betweenness_edge(_graph)


def _without_highest_betweenness_edge(graph):
    original_num_components = number_connected_components(graph)
    num_connected_components = original_num_components

    while num_connected_components <= original_num_components:
        # edges = get_edges_with_highest_betweenness(graph)
        #
        # for edge in edges:
        #     graph.remove_edge(*edge)

        edge = get_edges_with_highest_betweenness(graph)[0]
        graph.remove_edge(*edge)

        new_components = tuple(connected_components(graph))
        num_connected_components = len(new_components)

    return new_components


def _remove_self_loops(graph):
    for n, neighbors in graph.adj_list.items():
        if n in neighbors:
            graph.remove_edge(n, n)