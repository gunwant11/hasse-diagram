import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
num = [1,2,3,4,5,6,7,8,9,10,11,12]
nodes = []



pos = nx.spring_layout(G)
for i in range(1,len(num)+1):
    for j in range(1,len(num)+1):
        if i%j == 0:
            nodes.append((i,j))

nodes.remove((12,1))
nodes.remove((12,2))
nodes.remove((12,3))
nodes.remove((10,1))
nodes.remove((6,1))
nodes.remove((4,1))
nodes.remove((8,2))
nodes.remove((8,1))
nodes.remove((9,1))

print(nodes)
G.add_edges_from(nodes)
nx.draw(G,with_labels = True,node_shape = 'o')
print(nodes)

plt.show()
