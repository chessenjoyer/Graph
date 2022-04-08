import itertools
from matplotlib import pylab
import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt


from Graph_class import Graph
#Ввод из файла
graph= {}
data = []
with open("file.txt") as f:
     for line in f:
          line_new = line.strip ()
          data.append([int(x) for x in line_new.split(' ')])


vertex_number = int(data[0][0])
data.pop(0)
dict_list = []

for i in range(vertex_number):
     dict_list.append(int(i))
graph = dict(zip(dict_list,data))

#Рисуем граф
D = Graph(graph)
D.find_nodes()
D.DFS()
if D.cycle !=('not found cycle'):
     cycle = D.cycle


print(D.cycle)
print(D.centers)

colors = ['b' for i in range (vertex_number) ]
for i in D.centers:
     colors[i] ='r'
for i in cycle:
     if colors[i] == 'r':
          colors[i] = 'chocolate'
     else:
          colors[i] ='green'
visual_graph = nx.Graph()
#Заполняем Вершины
visual_graph.add_nodes_from(dict_list)
#Заполняем ребра
for k in graph.keys():
     for j in range (len(graph[k])):
          visual_graph.add_edge(k, graph[k][j])

nx.draw_planar(visual_graph,
     node_color=colors,
     node_size=900,
     with_labels=True)
plt.show()
