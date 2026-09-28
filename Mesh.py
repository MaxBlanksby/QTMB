from Layout import Layout


class Mesh(Layout):
    def __init__(self, num_qubits=0):
        super().__init__("mesh", num_qubits)
        self._build_graph()

    def _build_graph(self):
        
        rows = 6
        cols = 6

        # Add each qubit as a node
        for qubit_index in range(self.num_qubits):
            self.graph.add_node(qubit_index)

        # Add connections between neighboring qubits
        for row in range(rows):
            for col in range(cols):

                current = row * cols + col

                if current >= self.num_qubits:
                    continue

                # Connect to qubit on the right
                if col < cols - 1:
                    right = current + 1

                    if right < self.num_qubits:
                        self.graph.add_edge((current, right))

                # Connect to qubit below
                if row < rows - 1:
                    below = current + cols

                    if below < self.num_qubits:
                        self.graph.add_edge((current, below))