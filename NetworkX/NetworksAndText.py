import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()
G.add_edge('A', 'B')

# Set multiline labels
labels = {'A': 'This is line 1\nThis is line 2\nThis is line 3',
          'B': 'Another line\nAnd another line'}

# Calculate text sizes for each node label
label_sizes = {node: (len(text.split('\n')) * 100) for node, text in labels.items()}  # Adjust multiplier for font size

print(label_sizes)
# Draw the graph with nodes and edges, adjusting node sizes
pos = nx.spring_layout(G)
node_sizes = [label_sizes.get(node, 100) for node in G.nodes()]  # Default size 100 for nodes without labels
nx.draw(G, pos, with_labels=False, node_size=node_sizes, node_color='skyblue', edge_color='black')

# Draw multiline labels inside nodes
nx.draw_networkx_labels(G, pos, labels, font_size=8, font_color='black', font_weight='bold', verticalalignment='center', horizontalalignment='center')

if __name__ == '__main__':
    plt.axis('off')
    plt.show()
