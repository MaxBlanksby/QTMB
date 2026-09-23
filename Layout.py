from Graph import Graph


class Layout:
    def __init__(self, architecture_type, num_qubits):
        self.graph = Graph()
        self.architecture_type = architecture_type
        self.num_qubits = num_qubits
