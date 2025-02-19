import numpy as np

class Matrix:
    def __init__(self, matrix):
        self.matrix = np.array(matrix, dtype=float)
        self.size = len(matrix)

    def det_gauss(self):
        mat = self.matrix.copy()
        det : int = 1 # set determinant to 1 initially
        sign: int = 1 # check if the determinant is positive or negative
    
        for i in range(self.size):
            if mat[i, i] == 0: # select the pivot element(change the row if necessary)
                swap_found = False
                for k in range(i+1, self.size):
                    if mat[k, i] != 0:
                        mat[[i, k]] = mat[[k, i]] # swap the rows
                        sign *= -1 # change the sign of the determinant
                        swap_found = True
                        break
                if not swap_found:
                    return 0 # if the pivot element is 0, the determinant is 0

            # make zeros to below triangular matrix
            for j in range(i + 1, self.size):
                factor = mat[j, i] / mat[i, i]
                for k in range(i, self.size):
                    mat[j, k] = mat[j, k] - factor * mat[i, k]

            det *= mat[i, i] # multiply the determinant by the pivot element

        return det * sign # return the determinant


                