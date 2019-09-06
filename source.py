from graphio import create_colors, show

edges = [('a', 'b'), ('b', 'c'), ('a', 'c')]
node_color = create_colors(edges)
print(node_color)
# print(create_colors(edges))
show(edges, create_colors(edges))

