import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist("BMME590-2024/data/protein.edgelist.txt")

nx.draw_circular(G,node_size = 10, width = 0.3)

D = nx.density(G)
As = nx.degree_assortativity_coefficient(G)
Con = nx.is_connected(G)

print("The density of the network is",D)
print("The assortativity coefficient is",As)

if Con:
    print("The graph is connected.")
else:
    print("The graph is not connected.")

largest_cc = max(nx.connected_components(G), key=len)
print("The network diameter is", nx.diameter(largest_cc))

plt.show()


