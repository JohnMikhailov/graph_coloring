from graphio import show, read_edges
from hybrid.genetic import GeneticColoring
import networkx as nx


edges = read_edges('input.txt')
g = GeneticColoring(nx.Graph(edges))
g.build_coloring(fit=3, steps=50)
show(edges, g.get_rgb_coloring(), message=f'colors amount = {g.fit}')
