from graphio import create_colors
from random import shuffle, choice


class GeneticColoring:

    def __init__(self, graph):
        self.graph = graph
        self.nodes = self.graph.nodes
        self.edges = graph.edges
        self.colors = None
        self.node_color = {}

    def generate_colors(self):
        self.node_color = create_colors(self.edges)
        self.colors = list(self.node_color.values())

    def crossing_over(self, agent1, agent2):
        pass

    def mutation(self):
        colors = list(self.node_color.values())
        self.node_color = {node: choice(colors[1:]) for node in self.nodes}

    def is_valid(self):
        for i, j in self.edges:
            if self.node_color[i] == self.node_color[j]:
                return False
        return True

    def start(self, steps=1):
        self.generate_colors()
        valid_config = self.node_color.copy()
        for step in range(steps):
            self.mutation()
            if self.is_valid():
                valid_config = self.node_color.copy()
        self.node_color = valid_config.copy()

    def get_coloring(self):
        return self.node_color
