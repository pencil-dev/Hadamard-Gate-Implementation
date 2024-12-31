import pennylane as qml
import numpy as np

dev = qml.device('default.qubit', wires=1)

@qml.qnode(dev)
def hadamard_circuit():
    qml.Hadamard(wires=0)
    return qml.probs(wires=0)

result = hadamard_circuit()
print(f"Measurement probabilities: |0⟩: {result[0]}, |1⟩: {result[1]}")