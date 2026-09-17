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

    def drawdisplay(self):
        pass
        #make it use network x to display the whole graph
        G = nx.Graph()
        G.add_nodes_from(self.nodes)
        G.add_edges_from(self.edges)
        nx.draw(G, with_labels=True)
        plt.show()

