import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
num = [1,2,3,4,5,6,7,8,9,10,11,12]
nodes = []

#G.add_edges_from([('A','B'),('A','C'),('C','B')])

pos = nx.spring_layout(G)
for i in range(1,len(num)+1):
    for j in range(1,len(num)+1):
        #if i==j:
        #   nodes.append((i,j))
        if i%j == 0:
            nodes.append((i,j))
            #print(i,j)


prev = 0
nodes2 =[]
for a,b in nodes:
    for i in range(1, b + 1):
        if b % i == 0 and b != i:
            if i > prev:
                prev = i
                print((a,prev))
                # if nodes.count((a,prev)) > 0:
                #     nodes.remove((a,prev))
                #     print(a,prev,"hello")


            
    #print((a,b))

# for a,b in nodes:
#     for c,d in nodes:
#         if a == c and c != d:
#             #print((c,d))
#             nodes.remove((c,d))

    


G.add_edges_from(nodes)
nx.draw(G,with_labels = True,node_shape = 'o')
print(nodes)

plt.show()
