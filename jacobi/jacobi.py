import numpy as np

def jacobi_ij(A, i, j, e):
    
    n = A.shape[0]
    
    theta = 0.000001

    Jij = np.identity(n)

    if abs(A[i][j]) <= e:
        return Jij
    elif abs(A[i][i] - A[j][j]) <= e:
        theta = np.pi / 4
    else:
        theta = (1/2) * np.arctan( (-2*(A[i][j])) / (A[i][i] - A[j][j]))

    Jij[i][i] = np.cos(theta)
    Jij[j][j] = np.cos(theta)
    Jij[i][j] = np.sin(theta)
    Jij[j][i] = -np.sin(theta)

    return Jij

def jacobi_sweep(A, e):
    
    n = A.shape[0]
    J = np.identity(n)
    A_old = A
    
    for j in range(n - 1):
        for i in range(j + 1, n):
            Jij   = jacobi_ij(A_old, i, j, e)
            A_new = np.dot(np.dot(Jij.transpose(), A_old), Jij)
            A_old = A_new
            J = np.dot(J, Jij)

    return A_new, J

def sum_sqares_bellow_diag(A):
    
    size = A.shape[0]
    soma = 0
    for i in range(size):
        for j in range(size):
            if i < j:
                soma = soma + np.power(A[i][j], 2)
    return soma

def jacobi(A, e):
    
    n = A.shape[0]
    autovalores = np.zeros(n)
    val = 100
    J = np.identity(n)
    A_old = A

    while val > e:
        A_new, Ji = jacobi_sweep(A_old, e)
        A_old = A_new
        J = np.dot(J, Ji)
        val = sum_sqares_bellow_diag(A_new)
    
    for i in range(n):
        autovalores[i] = A_new[i][i]

    return autovalores, J

A = np.array([
    [-40, 8, 4, 2, 1],
    [8, -30, 12, 6, 2],
    [4, 12, 20, 1, 2],
    [2, 6, 1, 25, 4],
    [1, 2, 2, 4, 5]])

C, J = jacobi(A, 0.000001)

print(J)

print("\n\n\nCOMPARACAO COM NUMPY\n\n\n")

print(np.linalg.eig(A))
