# Hadamard Gate Superposition

Creates an equal superposition state using the Hadamard gate.

## Requirements
```
pennylane>=0.19.0
numpy>=1.19.0
```

## Implementation
- Applies Hadamard gate to |0⟩ state
- Creates superposition: |ψ⟩ = (|0⟩ + |1⟩)/√2
- Measures in computational basis

## Expected Output
- |0⟩: 0.5 (50% probability)
- |1⟩: 0.5 (50% probability)

## Usage
```python
python hadamard_gate.py
```
