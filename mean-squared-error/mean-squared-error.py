import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    pred = np.array(y_pred, dtype='f') # S, O
    true = np.array(y_true, dtype='f') # S, O
    error = pred - true                # S, O   
    serror=  error ** 2
    mse = np.sum(serror) / len(serror)
    return mse
