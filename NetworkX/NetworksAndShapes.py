import networkx as nx
import matplotlib.pyplot as plt

# Code to create a BA network using networkx and assigning different shapes and colours to various nodes

if __name__ == '__main__':
    n = 10
    m = 2

    G = nx.barabasi_albert_graph(n, m)

    # Define nodes to be displayed as squares and circles
    square_nodes = [0, 1, 2]
    circle_nodes = [node for node in G.nodes() if node not in square_nodes]

    pos = nx.spring_layout(G)  # Layout for visualization

    # Draw circles first
    nx.draw_networkx_nodes(G, pos, nodelist=circle_nodes, node_shape='o', node_color='red', node_size=200)

    # Then draw squares
    nx.draw_networkx_nodes(G, pos, nodelist=square_nodes, node_shape='s', node_color='blue', node_size=200)

    # Draw edges and labels
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)

    # Show the plot
    plt.show()
