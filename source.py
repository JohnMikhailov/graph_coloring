from graphio import show
from genetic.coloring import GeneticColoring
import networkx as nx


edges = [('a', 'b'), ('b', 'c'), ('a', 'c'), ('c', 'd')]
g = GeneticColoring(nx.Graph(edges))
n = g.start(100)
show(edges, g.get_coloring(n))
