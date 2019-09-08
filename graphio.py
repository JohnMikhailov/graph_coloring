import networkx as nx
import matplotlib.pyplot as plt

'''
        Считываение графа

        Формат графа в файле: каждая строка файла - два обозначения, разделенных пробелом
        Вершиной графа может быть число, слово, буква, символ и тд

        Пример файла:

        a b
        a c
        b c

'''


def read_edges(path='input.txt'):  # path - путь к файлу, input.txt - значение по умолчанию
    with open(path) as inputs:
        edges = [tuple(i.strip().split()) for i in inputs.readlines()]  # считываем все строки из файла
        #  получаем список строк, для примера выше список будет выглядеть так: ['a b', 'a c', 'b c']
        #  i.strip() - убирает пробелы, табы и переносы строки
        #  split() - разделяет строку по пробелу (можно указать любой символ, по умолчанию - пробел)
        #  в итоге: edges = [('a', 'b'), ('a', 'c'), ('b', 'c')]
    return edges


def write_edges(path='output.txt'):
    pass


# входной граф - список ребер
# если взять пример выше, то edges представлется так: edges = [('a', 'b'), ('a', 'c'), ('b', 'c')]
# node_color = {node: 'color'}
def show(edges, node_color, message='Colored graph', with_labels=True):  # отображает граф
    #  цвета представляются в виде целых чисел, больших 1
    g = nx.Graph()
    g.add_edges_from(edges)
    pos = nx.spring_layout(g)
    for node, color in node_color.items():
        nx.draw(g, pos, nodelist=[node], node_color=color, with_labels=with_labels)
    plt.gcf().canvas.set_window_title(message)
    plt.show()
