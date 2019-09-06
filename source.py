from graphio import show
from genetic.coloring import GeneticColoring
import networkx as nx


edges = [('a', 'b'), ('b', 'c'), ('a', 'c'), ('c', 'd'), ('a', 'd'), ('a', 'e')]
g = GeneticColoring(nx.Graph(edges))
g.start(100)
nc = g.node_color
show(edges, nc)
