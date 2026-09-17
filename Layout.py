import Graph


class Layout:
    def __init__(self):
        self.G = Graph.Graph()


    def add_node(self, node):
        self.G.add_node(node)

    def add_edge(self, edge):
        self.G.add_edge(edge)

    def get_nodes(self):
        return self.G.get_nodes()

    def get_edges(self):
        return self.G.get_edges()

    def draw(self):
        self.G.drawdisplay()
