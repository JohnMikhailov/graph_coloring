from random import shuffle, random
from itertools import cycle


class GeneticColoring:

    def __init__(self, graph):
        self.graph = graph
        self.nodes = self.graph.nodes
        self.edges = graph.edges
        self.node_color = {}

    def is_valid(self):
        for i, j in self.edges:
            if self.node_color[i] == self.node_color[j]:
                return False
        return True

    def apply_colors(self, colors):
        shuffle(colors)
        color = cycle(colors)
        self.node_color = {node: next(color) for node in self.nodes}

    def start(self, steps=1):
        colors = list(range(len(self.nodes)))
        self.apply_colors(colors)
        saved_colors = []
        valid_config = {}
        for step in range(steps):
            if self.is_valid():
                saved_colors = colors.copy()
                valid_config = self.node_color
                colors.pop()
                self.apply_colors(colors)
            else:
                colors = saved_colors.copy()
                self.node_color = valid_config
        if not self.is_valid():
            self.node_color = valid_config
        return len(colors)

    def fitness(self):
        pass

    def get_coloring(self):
        rgb = {color: ((color / len(self.nodes)) * random(), random(), random()) for color in self.node_color.values()}
        return {node: rgb[self.node_color[node]] for node in self.nodes}
