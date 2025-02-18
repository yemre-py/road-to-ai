def det_gauss(A, n):
    det : int = 1 # set determinant to 1 initially
    sign: int = 1 # check if the determinant is positive or negative
    
    for i in range(n):
        if A[i][i] == 0: # select the pivot element(change the row if necessary)
            swap_found = False
            for k in range(i+1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i] # swap the rows
                    sign = sign * (-1) # change the sign of the determinant
                    swap_found = True
                    break
            if not swap_found:
                return 0 # if the pivot element is 0, the determinant is 0
        
        # make zeros to below triangular matrix
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] = A[j][k] - factor * A[i][k]
        
        det = det * A[i][i] # multiply the determinant by the pivot element
    
    return det * sign # return the determinant


