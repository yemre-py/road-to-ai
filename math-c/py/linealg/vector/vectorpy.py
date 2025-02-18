# vector operations but more pythonic
from functools import reduce

def dot_product(*vectors):
    if len(vectors)<2:
        raise ValueError("at least two vectors required")
    
    get_first_size = len(vectors[0])
    
    if any(len(vector) != get_first_size for vector in vectors):
        raise ValueError("all vectors must be the same size")
    
    return sum(reduce(lambda x, y: x*y, elems) for elems in zip(*vectors))
