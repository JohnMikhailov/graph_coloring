from collections import Counter
from random import choice

from hybrid.mixins import GeneticMixin, GetColoringMixin


class SwarmOptimization(GeneticMixin, GetColoringMixin):

    def __init__(self, graph, node_color):
        self.colors = list(node_color.values())  # список целых чисел, наприемр colors = [4, 3, 1, 2]
        self.graph = graph
        self.edges = graph.edges
        self.nodes = graph.nodes
        self.instinct = {i: 1 for i in range(len(self.colors))}
        self.colors_count = Counter(self.colors)
        self.node_color = node_color
        self.node_color_save = None
        self.rgb = None
        self.rgb_coloring = None

    def optimize(self, steps=1, greedy_level=1, population_size=1):
        colors = self.colors
        q = greedy_level
        p = population_size
        self.node_color_save = self.node_color.copy()
        for step in range(steps):

            props = []
            for i, color in enumerate(self.colors):
                prop = ((self.colors_count[color]**q) * (self.instinct[i]**p))
                prop_sum = sum([((self.colors_count[color]**q) * (self.instinct[i]**p)) for i in range(len(colors))])
                props.append(prop / prop_sum)

            i = props.index(max(props))

            valid = self.is_coloring_valid()
            if valid:
                colors = self.colors.copy()
                self.node_color_save = self.node_color.copy()
                self.mutate(colors, i)
            else:
                self.node_color = self.node_color_save.copy()
                self.colors = colors.copy()
            self.__update(valid)

    def __update(self, valid):
        coeff = 0.1 if valid else -0.1
        for i in self.instinct:
            tmp = self.instinct[i] + coeff
            if tmp != 0:
                self.instinct[i] += coeff
        self.colors_count = Counter(self.colors)
