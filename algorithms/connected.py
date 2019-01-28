"""
Helper functions to detect connected components in Graph objects
"""

# Reference: https://github.com/networkx

from model.graph import Graph


def number_connected_components(graph: Graph):
    return sum(1 for c in connected_components(graph))


def connected_components(graph: Graph):
    visited = set()
    for v in graph.nodes:
        if v not in visited:
            component = set(_bfs(graph, v))
            yield component
            visited.update(component)


def _bfs(graph: Graph, initial_vertex: int):
    adj = graph.adj_list
    visited = set()
    next_level = {initial_vertex}
    while next_level:
        current_level = next_level
        next_level = set()
        for v in current_level:
            if v not in visited:
                yield v
                visited.add(v)
                next_level.update(adj[v])