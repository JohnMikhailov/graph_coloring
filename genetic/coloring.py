from random import shuffle, choice, random
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

    def initialize_colors(self, colors):
        self.node_color = {node: color for node, color in zip(self.nodes, colors)}

    def apply_colors(self, colors):
        shuffle(colors)
        color = cycle(colors)
        self.node_color = {node: next(color) for node in self.nodes}

    def start(self, steps=1):
        colors = list(range(len(self.nodes)))
        self.initialize_colors(colors)
        saved_colors = []
        for step in range(steps):
            if self.is_valid():
                saved_colors = colors.copy()
                colors.pop()
                self.apply_colors(colors)
            else:
                colors = saved_colors.copy()
        return len(colors)

    def fitness(self):
        pass

#TODO: вынести одинаковые цвета!!! все цвета получаются разными из-за рандома
# один и тот же цвет получается в итоге с разными оттенками

    def get_coloring(self, fit):
        return {node: ((int_color / fit) * random(), random(), random()) for node, int_color in self.node_color.items()}
