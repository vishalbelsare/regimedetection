"""
Provide similarity metrics as described in the paper
'A New Approach to Data-Driven Clustering'

Functions provided here should be non-negative, monotonically
decreasing functions
"""

import numpy as np


def make_gaussian_similarity(sigma):
    sigma_squared = sigma * sigma

    def gaussian_similarity(x):
        return np.exp(-x / sigma_squared)

    return gaussian_similarity


def make_gaussian_similarity_from_percentile(distances, percentile):
    sigma = np.percentile(distances, percentile)
    return make_gaussian_similarity(sigma)
