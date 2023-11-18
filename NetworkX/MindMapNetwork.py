import networkx as nx
import matplotlib.pyplot as plt
import random
import os


def generate_mindmap(n, m, k):
    G = nx.star_graph(n)
    center_node = max(G.nodes(), key=G.degree)

    nodes = set(G.nodes())
    num_nodes = len(nodes)

    nodes = nodes - {center_node}

    for i in range(m):
        random_node = random.choice(list(nodes))
        nodes = nodes - {random_node}

        for j in range(k):
            G.add_node(num_nodes)
            G.add_edge(random_node, num_nodes)
            num_nodes += 1

    return G


if __name__ == '__main__':
    G = generate_mindmap(5, 3, 3)

    layout = nx.layout.spring_layout(G)

    square_nodes = random.sample(list(G.nodes()), 5)
    non_square_nodes = set(G.nodes()) - set(square_nodes)

    nx.draw_networkx(G, layout, nodelist=square_nodes, node_shape='s', node_size=1500)
    nx.draw_networkx(G, layout, nodelist=non_square_nodes, node_shape='o', node_size=1500)

    plt.savefig(os.path.join("./NetworkX/data", "sample_image.png"))
    plt.show()
