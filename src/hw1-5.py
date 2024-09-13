import networkx as nx


p = .04 # 0.4 probability gives the closest average degree to that of part 1

G = nx.binomial_graph(100, p)

deg = nx.degree(G)

sum_deg = 0
for node in range(0,100):
        sum_deg = sum_deg + deg(node,2)
avg_deg = sum_deg/100

print(avg_deg)
