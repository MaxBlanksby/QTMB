from Solution import Solution


native_gate_set = ["H", "X", "Y", "Z", "CNOT"]
solution = Solution("heavyhex", native_gate_set, num_qubits=6)
solution.describe(print_to_terminal=True)
solution.visualize()