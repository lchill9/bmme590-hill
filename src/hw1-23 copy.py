import networkx as nx
import random
import matplotlib.pyplot as plt


N = 100
E = 200

G = nx.Graph()

for node in range(1,N+1):
	G.add_node(node)

for edge in range(1,E+1):
	B = False
	while not B:
		n1 = random.randint(1,N)
		n2 = random.randint(1,N)

		if (n1, n2) not in G.edges and (n2, n1) not in G.edges:
			B = True
			G.add_edge(n1,n2)	

D = nx.density(G)
deg = nx.degree(G)
sum_deg = 0
for node in range(1,N+1):
        sum_deg = sum_deg + deg(node,2)
avg_deg = sum_deg/N     


print("The density of the network is", D)
print("The mean degree is", avg_deg)
print("Degree distribution:",nx.degree_histogram(G))

nx.draw(G)
plt.show()




