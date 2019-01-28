"""Visualisation functions for community scanner"""

import matplotlib.pyplot as plt
from networkx import nx
from model.graph import Graph

__author__ = "Eduardo Hernandez"
__email__ = "https://www.linkedin.com/in/eduardohernandezj/"


def draw(graph: Graph, components):
    """Draw the graph showing edge weight

    :param graph: graph object to draw
    :param components: tuple of sets, where each set represents a set of nodes
    """

    graph_nx = nx.Graph()
    graph_nx.add_weighted_edges_from(graph.weighted_edges)

    labels = nx.get_edge_attributes(graph_nx, 'weight')
    pos = nx.spring_layout(graph_nx)
    community_map = get_community_map(components)

    nx.draw_networkx(
        graph_nx, pos=pos,
        with_labels=False,
        node_size=200, node_shape="o",
        node_color=list(community_map.values())

    )

    plt.get_cmap()
    plt.axis('off')
    plt.title(graph.name)
    plt.show()


def draw_small_graph(graph):
    """Draw the graph showing edge weight
    :param graph: graph object to draw
    """

    graph_nx = nx.Graph()
    graph_nx.add_weighted_edges_from(graph.weighted_edges)

    labels = nx.get_edge_attributes(graph_nx, 'weight')
    pos = nx.spring_layout(graph_nx)
    nx.draw_networkx_edge_labels(
        graph_nx, pos=pos,
        edge_labels=labels
    )

    nx.draw(graph_nx, pos=pos,
            with_labels=True, node_size=10,
            node_color="skyblue", node_shape="o",
            alpha=0.5, linewidths=30)

    plt.title(graph.name)
    plt.show()


def get_community_map(components):
    community_map = dict()

    for index, community in enumerate(components):
        for node in community:
            community_map[node] = index

    return community_map


def main():
    """Draw a sample graph"""
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 5)]
    graph = Graph('Visualizer Sample')
    graph.add_nodes(nodes)
    graph.add_edges(edges)
    draw(graph)


if __name__ == '__main__':
    main()
