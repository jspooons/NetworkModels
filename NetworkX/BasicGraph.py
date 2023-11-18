import networkx as nx
import matplotlib.pyplot as plt

# This class implements an undirected graph
G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2,3])

G.add_edge(1, 2)
G.add_edge(1, 3)


if __name__ == '__main__':
    nx.draw(G)
    plt.show()
