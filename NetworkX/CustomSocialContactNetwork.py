import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


def social_network(n, initial, growth, max_degree):
    # Function for creating a Barabasi-Albert (BA) network model
    # It has been derived from my matlab code used in the Particle-Based-Covid19-Simulator repository
    # in social_network.m

    N = n  # Number of nodes in the network
    adj_matrix = np.zeros((N, N), dtype=int)  # Adjacency matrix for the network
    nodes = list(range(1, N + 1))  # Nodes in the network
    cdf = np.zeros(N)  # Cumulative distribution function for node degrees
    m0 = initial  # Initial number of connected nodes
    m = growth  # Number of edges to attach from a new node to existing nodes
    max_deg = max_degree  # Maximum degree allowed for a node

    # Select m0 nodes randomly to start the network
    r = random.sample(range(1, N + 1), m0)
    nodes = list(set(nodes) - set(r))
    random.shuffle(nodes)

    # Initial connections between the selected nodes
    for i in range(m0):
        tmp = list(set(r) - {r[i]})
        rand_i = np.random.randint(1, m0)
        if adj_matrix[r[i] - 1, tmp[rand_i - 1] - 1] != 1:
            adj_matrix[r[i] - 1, tmp[rand_i - 1] - 1] = 1
            adj_matrix[tmp[rand_i - 1] - 1, r[i] - 1] = 1

    degrees = np.sum(adj_matrix, axis=0)  # Degrees of nodes in the network

    # Calculate the cumulative distribution function (CDF) of node degrees
    prev = 0
    for i in range(N):
        cdf[i] = degrees[i] / np.sum(degrees) + prev
        prev = cdf[i]

    # Growing the network using the Barabási-Albert algorithm
    for i in range(N - m0):
        for j in range(m):
            rand_p = np.random.rand()  # Random probability
            prev = 0
            for k in range(N):
                if prev < rand_p <= cdf[k]:
                    adj_matrix[nodes[i] - 1, k] = 1  # Add an edge
                    adj_matrix[k, nodes[i] - 1] = 1  # Add an edge
                    degrees[nodes[i] - 1] += 1  # Update degrees
                    degrees[k] += 1  # Update degrees
                    break
                prev = cdf[k]

        total = np.sum(degrees[degrees >= max_deg])  # Total degrees exceeding the maximum degree
        prev = 0

        # Update the cumulative distribution function (CDF) after adding new nodes
        for k in range(N):
            d = 0
            if degrees[k] < max_deg:
                d = degrees[k]
            cdf[k] = d / (np.sum(degrees) - total) + prev
            prev = cdf[k]

    return adj_matrix


if __name__ == '__main__':
    A = social_network(10, 2, 2, 4)
    G = nx.from_numpy_array(A, parallel_edges=True, create_using=nx.Graph())

    nx.draw(G)
    plt.show()
