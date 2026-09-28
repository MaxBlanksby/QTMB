from Solution import Solution
import qiskit as q






num_qubits = 36
qc = q.QuantumCircuit(num_qubits)



qc.x(0)
print(qc)


native_gate_set = ["H", "X", "Y", "Z", "CNOT"]
solution = Solution("mesh", native_gate_set, num_qubits=num_qubits)
solution.describe(print_to_terminal=True)
solution.visualize()