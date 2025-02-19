from functools import reduce

import numpy as np


class Vector:
    def __init__(self, *vectors):
        self.vectors = np.array(vectors, dtype=float)
        self.size = self.vectors.shape[1]
        
    def linear_combination(self, *coefficients):
        if len(self.vectors) < 2:
            raise ValueError("You must provide at least two vectors")
        
        if len(coefficients) != len(self.vectors):
            raise ValueError("The number of coefficients must be equal to the number of vectors")
        
        return np.sum(coef * vec for coef, vec in zip(coefficients, self.vectors))

    def dot_product(self):
        if len(self.vectors) < 2:
            raise ValueError("You must provide at least two vectors")
        
        if any( len(vector) != self.size for vector in self.vectors):
            raise ValueError("All vectors must have the same size")
        
        return np.sum(reduce(lambda x, y: x*y, elems) for elems in zip(*self.vectors))
    
    def length(self):
        if len(self.vectors) > 1:
            raise ValueError("You must just provide one vector")
        
        return np.sqrt(np.sum(np.square(self.vectors)))
    
