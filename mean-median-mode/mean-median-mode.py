import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    count = Counter(x)
    x = np.array(x)
    mean = np.mean(x)
    median = np.median(x)
    freq = max(count.values())
    mode = np.min([k for k, v in count.items() if v == freq])
    return (mean, median, mode)