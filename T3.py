from itertools import combinations
import numpy as np


def mean(arr):
    return np.mean(arr)


def median(arr):
    return np.median(arr)


def max_weight_val(n, a):
    max_val = float('-inf')
    for length in range(1, n + 1):
        for subsequence in combinations(a, length):
            mean_val = mean(subsequence)
            median_val = median(subsequence)
            weight_val = mean_val - median_val
            max_val = max(max_val, weight_val)

    return max_val



#test
n = 4
a = [1, 3, 5, 9]
print(max_weight_val(n, a))
