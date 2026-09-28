from Solution import Solution
import qiskit as q






num_qubits = 9
qc = q.QuantumCircuit(num_qubits)



qc.x(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(0, 8)
qc.cx(8, 0)
qc.h(0)
print(qc)


native_gate_set = ["H", "X", "Y", "Z", "CNOT"]
solution = Solution("mesh", native_gate_set, num_qubits=num_qubits)
solution.describe(print_to_terminal=True)
solution.visualize()