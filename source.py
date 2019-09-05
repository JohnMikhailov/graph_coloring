import networkx as nx

g = nx.Graph()
g.add_edges_from([('a', 'b'), ('a', 'c'), ('b', 'c')])
pos = nx.spring_layout(g)
nx.draw(g, pos)
