from graphio import show, read_edges
from hybrid.genetic import GeneticColoring
from hybrid.swarm import SwarmOptimization
import networkx as nx


edges = read_edges('input.txt')
g = GeneticColoring(nx.Graph(edges))
g.build_coloring(fit=3, steps=50)
show(edges, g.get_rgb_coloring(), message=f'colors amount = {g.fit}')

# s = SwarmOptimization(nx.Graph(edges), g.get_int_coloring())
# s.optimize(10, 1, 1)
#
# coloring = s.get_rgb_coloring()
#
# show(edges, coloring, message=f'colors amount = {g.fit}')
