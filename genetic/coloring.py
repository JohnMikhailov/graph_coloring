from random import shuffle, random, randint
from itertools import cycle


class GeneticColoring:

    def __init__(self, graph):
        self.graph = graph
        self.nodes = self.graph.nodes
        self.edges = graph.edges
        self.node_color = {}
        self.fit = None
        self.rgb = None

    def __is_coloring_valid(self):
        for i, j in self.edges:
            if self.node_color[i] == self.node_color[j]:
                return False
        return True

    def __mutate(self, colors):
        color = cycle(colors)
        self.node_color = {node: next(color) for node in self.nodes}

    def __fitness(self):
        return len(set(self.node_color.values()))

    def start(self, fit, steps=1):
        colors = list(range(len(self.nodes)))
        self.__mutate(colors)
        valid_config = {}
        for step in range(steps):
            if self.__is_coloring_valid():
                if self.__fitness() <= fit:  # минимизация
                    self.fit = fit
                    return None
                valid_config = self.node_color
                colors.pop()
                self.__mutate(colors)
            else:
                self.node_color = valid_config
                colors = list(valid_config.values())
                shuffle(colors)  # если этого не сделать, то цвета будут возвращаться в том же порядке
                # и в итоге реузльтат не изменится
        if not self.__is_coloring_valid():
            self.node_color = valid_config
        self.fit = len(set(self.node_color.values()))
        return None

    def get_coloring(self):
        self.rgb = {color: ((color / len(self.nodes)) * random(), random(), random()) for color in self.node_color.values()}
        return {node: self.rgb[self.node_color[node]] for node in self.nodes}
