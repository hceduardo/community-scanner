"""Common configuration"""

import os

__author__ = "Eduardo Hernandez"
__email__ = "https://www.linkedin.com/in/eduardohernandezj/"


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

TESTS_IN_DIR = os.path.join(BASE_DIR, "tests", "test_graphs")

# maximum numbers of edges to be parsed.
EDGES_LIMIT = 1000

# Level of communities in Girvan-Newman algorithm
# Defines number of communities desired
COMPONENTS_LEVEL = 3

# If true, all levels of components are displayed until the level of each node is a community itself
DISPLAY_ALL_COMPONENTS = False

# If True, the graph will be visualised. Keep false for graphs with more than 100 edges
DRAW = True

