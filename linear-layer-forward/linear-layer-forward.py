import numpy as np
def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    X = np.array(X)
    W = np.array(W)
    b = np.array(b)
    ans = X @ W + b
    return [ list(row) for row in ans]