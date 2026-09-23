import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def printdisplay(self):
        print("Nodes:", self.nodes)
        print("Edges:", self.edges)

    def drawdisplay(self, title="Qubit Connectivity", show=True):
        graph = nx.Graph()
        graph.add_nodes_from(self.nodes)
        graph.add_edges_from(self.edges)

        figure, axis = plt.subplots(figsize=(8, 6))
        positions = nx.spring_layout(graph, seed=42)
        nx.draw_networkx(
            graph,
            pos=positions,
            ax=axis,
            with_labels=True,
            node_color="#8ecae6",
            edge_color="#4f5d75",
            node_size=1100,
            font_weight="bold",
        )
        axis.set_title(title)
        axis.set_axis_off()
        figure.tight_layout()

        if show:
            plt.show()

        return figure

