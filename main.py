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


# prev = 1
# nodes2 =[]
# for a,b in nodes:
#     for i in range(1, b + 1):
#         if b % i == 0 and b != i:
#             if i > prev:
#                 prev = i
#                 print((a,prev))
#                 # if nodes.count((a,prev)) > 0:
#                 #     nodes.remove((a,prev))
#                 #     print(a,prev,"hello")


            
    #print((a,b))
# y=0
# def print_factors(x):
#     print("The factors of",x,"are:")
#     for i in range(2, x + 1):
#        if x % i == 0:
#             y = y+1
#     print(y)


for a,b in nodes:
    for c,d in nodes:
        if a == c and c != d:
            print((c,d))
            
            # if print_factors(d) > 2:
            #     print("factssssss")
            #     pass

            #nodes.remove((c,d))
# def isprime(num):
#     for n in range(2,int(num**1/2)+1):
#         if num%n==0:
#             return True
#     return False

# for a,b in nodes:
#     if (isprime(a)):
#         nodes.remove((a,1))


nodes.remove((12,1))
nodes.remove((12,2))
nodes.remove((12,3))
nodes.remove((10,1))
nodes.remove((6,1))
nodes.remove((4,1))
nodes.remove((8,2))
nodes.remove((8,1))
nodes.remove((9,1))
G.add_edges_from(nodes)
nx.draw(G,with_labels = True,node_shape = 'o')
print(nodes)

plt.show()
