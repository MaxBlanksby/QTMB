from Heavyhex import Heavyhex
from Mesh import Mesh


class Solution:
    _architecture_types = {
        "heavyhex": Heavyhex,
        "mesh": Mesh,
    }


    #constructor
    def __init__(self, architecture_type, native_gate_set, num_qubits):
        try:
            layout_type = self._architecture_types[architecture_type.lower()]
        except AttributeError as error:
            raise TypeError("architecture_type must be a string") from error
        except KeyError as error:
            available_types = ", ".join(self._architecture_types)
            raise ValueError(
                f"Unsupported architecture type: {architecture_type}. "
                f"Choose one of: {available_types}."
            ) from error

        self.layout = layout_type(num_qubits)
        self.native_gate_set = list(native_gate_set)



    def describe(self, print_to_terminal=False):
        """Return the target architecture description for later circuit transpilation."""
        transpiled_architecture = {
            "architecture_type": self.layout.architecture_type,
            "num_qubits": self.layout.num_qubits,
            "native_gate_set": self.native_gate_set,
            "coupling_map": self.layout.graph.get_edges(),
        }

        if print_to_terminal:
            print(transpiled_architecture)

        return transpiled_architecture

    def visualize(self):
        title = f"{self.layout.architecture_type.title()} Architecture"
        return self.layout.graph.drawdisplay(title=title, show=True)

        



        