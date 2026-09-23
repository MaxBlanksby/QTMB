import Graph


class Layout:
    def __init__(self, layoutName, numqubits):
        self.G = Graph.Graph()
        self.layout_algorithm = layoutName
        self.numqubits = numqubits
