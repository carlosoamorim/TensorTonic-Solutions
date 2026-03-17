import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x, dtype=float)
    p = np.array(p, dtype=float)

    if x.shape != p.shape:
        raise ValueError(f"Shape mismatch: x={x.shape}, p={p.shape}")

    if abs(p.sum() - 1.0) > 1e-6:
        raise ValueError(f"Probabilities must sum to 1, got {p.sum()}")

    return float(np.dot(x, p))