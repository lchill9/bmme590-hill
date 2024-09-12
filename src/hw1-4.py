import networkx as nx
import random

N = int(input("How many nodes?  "))
E = int(input("How many edges?  "))

G = nx.DiGraph()

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
	
A = nx.adjacency_matrix(G)
print("Adjacency matrix:",A)





