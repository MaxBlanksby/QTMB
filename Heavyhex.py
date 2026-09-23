from Layout import Layout


class Heavyhex(Layout):
    def __init__(self, num_qubits=6):
        super().__init__("heavyhex", num_qubits)
        self._build_graph()

    def _build_graph(self):
        for qubit_index in range(self.num_qubits):
            self.graph.add_node(f"Q{qubit_index}")

        # Placeholder topology: replace with the complete heavy-hex generator.
        for qubit_index in range(self.num_qubits - 1):
            self.graph.add_edge((f"Q{qubit_index}", f"Q{qubit_index + 1}"))




