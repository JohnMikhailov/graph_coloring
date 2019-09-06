import networkx as nx
from graphio import create_colors
from random import shuffle, choice


class GeneticColoring:

    def __init__(self, edges):
        self.graph = nx.Graph(edges)
        self.nodes = self.graph.nodes
        self.edges = edges
        self.colors = None
        self.node_color = {}

    def generate_colors(self):
        self.colors = create_colors(self.edges)

    def set_colors_to_graph(self, colors):
        self.node_color = {node: choice(colors) for node in self.nodes}


    def crossing_over(self, agent1, agent2):
        pass

    def mutation(self, agent):
        pass

    def start(self, steps=1, population=2):
        pass







