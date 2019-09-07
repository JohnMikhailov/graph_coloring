from graphio import show, read_edges
from genetic.coloring import GeneticColoring
import networkx as nx


edges = read_edges('input.txt')
g = GeneticColoring(nx.Graph(edges))
print(g.start(fit=3, steps=500))
show(edges, g.get_coloring())
