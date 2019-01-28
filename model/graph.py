"""Class for undirected graphs"""

from sys import getsizeof

__author__ = "Eduardo Hernandez"
__email__ = "https://www.linkedin.com/in/eduardohernandezj/"

class Graph(object):
    #ToDo: optimise object size: remove nodes list and make adjacency list only one way.

    def __init__(self, name):
        self._name = name
        self._nodes = list()
        self._adj_list = dict()

    def add_nodes(self, nodes):
        for n in nodes:
            if n not in self._nodes:
                self._nodes.append(n)
                self._adj_list[n] = dict()

    def add_edges(self, edges):
        for e in edges:
            ne = len(e)
            if ne != 3:
                raise TypeError("Edge tuple %s must be a 3-tuple." % (e,))

            u, v, weight = e

            if u not in self._nodes:
                self._nodes.append(u)
                self._adj_list[u] = dict()

            if v not in self._nodes:
                self._nodes.append(v)
                self._adj_list[v] = dict()

            if u != v:
                self._adj_list[u][v] = weight
                self._adj_list[v][u] = weight

    def copy(self):
        graph = self.__class__(name=self._name)
        graph.add_nodes(self._nodes.copy())
        graph.add_edges(
            (u, v, w)
            for u, neighbors in self._adj_list.items()
            for v, w in neighbors.items()
        )
        return graph

    @property
    def nodes(self):
        return self._nodes

    @property
    def edges(self):
        visited = {}

        for u, neighbors in self._adj_list.items():
            for v in neighbors:
                if v not in visited:
                    yield (min(u, v), max(u, v))

            visited[u] = 1

        del visited

    @property
    def weighted_edges(self):
        visited = {}

        for u, neighbors in self._adj_list.items():
            for v, w in neighbors.items():
                if v not in visited:
                    yield (min(u, v), max(u, v), w)

            visited[u] = 1

        del visited

    @property
    def name(self):
        return self._name

    @property
    def adj_list(self):
        return self._adj_list

    def number_of_edges(self):
        # sum of the neighbors size of each vertex
        neighbor_size_sum = sum(len(neighbors) for v, neighbors in self._adj_list.items() )

        # each edge appear twice in adjacency list (once per node)
        return neighbor_size_sum // 2

    def remove_edge(self, u, v):
        try:
            del self._adj_list[u][v]

            if u != v:  # if not self loops
                del self._adj_list[v][u]
        except:
            raise ValueError("The edge (%s,%s) is not in the graph" % (u, v))

    def __sizeof__(self):
        size = 0

        size += getsizeof()

        return size
