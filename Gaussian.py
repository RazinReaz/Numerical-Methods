import numpy as np


def gaussianElimination(mat):
    '''
    mat is the augmented matrix. n is the number of equations.
    returns an array of n elements (considering #equations == #unknowns)
    '''
    n = rows = mat.shape[0]
    cols = mat.shape[1]

    if(cols-rows != 1 or mat.ndim != 2):
        return "Improper dimension of augmented matrix"

    for i in range(n-1):
        #partial pivoting
        max = abs(mat[i,i])
        max_row = i
        for j in range(i+1,n):
            if(abs(mat[j,i]) > max):
                max = abs(mat[j, i])
                max_row = j
        mat[[i,max_row],:] = mat[[max_row,i],:] #swapping the row with the max element

        #elimination
        pivot = mat[i, i]
        
        if(pivot == 0):
            return "No unique solution exist"
        for j in range(i+1, n):
            m = mat[j, i]*1.0/pivot
            mat[j] = mat[j]-m*mat[i]
    
    for i in range(rows):
        if(mat[i,i] == 0):
            return "No unique solution exist"

    A = mat[:, 0:cols-1]
    b = mat[:, cols-1].reshape(n, 1)
    x = np.ones((n, 1))

    #Back substitution
    for i in range(rows-1, -1, -1):
        x[i, 0] = (b[i, 0] + A[i, i] - A[i].dot(x)[0])/A[i, i]
    return x


if __name__ == "__main__":
    a = np.array([[1, 2, 3], [2, 4, 9]], dtype=np.float64)
    print(gaussianElimination(a))
