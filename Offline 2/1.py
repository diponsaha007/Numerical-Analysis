import numpy as np


def printMatrix(a, n, fopen):
    for i in range(n):
        round_values = np.around(a[i], decimals=4)
        for j in round_values:
            fopen.write(str(j))
            fopen.write(" ")
        fopen.write("\n")
    fopen.write("\n")


def printArray(a, n, fopen, newline=True):
    for i in range(n):
        round_values = np.around(a[i], decimals=4)
        fopen.write(str(round_values))
        if i == n - 1 and not newline:
            continue
        fopen.write("\n")
    if newline:
        fopen.write("\n")


def hasSolution(a, n, fopen):
    for i in range(n):
        flag = False
        for j in range(n):
            if a[i][j] != 0:
                flag = True
                break
        if flag == False:
            fopen.write("No unique solution\n")
            fopen.close()
            exit(1)


def take_input():
    # Taking input from file
    fopen = open("in1.txt", "r")
    line = fopen.readline()
    n = int(line)
    A_matrix = []
    B_matrix = []

    for i in range(n):
        line = fopen.readline()
        A_matrix.append([float(x) for x in line.split(' ')])

    for i in range(n):
        line = fopen.readline()
        B_matrix.append(float(line))

    fopen.close()

    A_matrix = np.array(A_matrix)
    B_matrix = np.array(B_matrix)
    return A_matrix, B_matrix, n


def constitute_LU(A_matrix, n):
    L_matrix = np.zeros([n, n])
    U_matrix = np.zeros([n, n])

    # Constituting L and U matrix
    U_matrix = A_matrix
    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = U_matrix[i][k] / U_matrix[k][k]
            L_matrix[i][k] = factor
            for j in range(k + 1, n):
                U_matrix[i][j] = U_matrix[i][j] - factor * U_matrix[k][j]
            for j in range(k + 1):
                U_matrix[i][j] = 0

    for i in range(n):
        L_matrix[i][i] = 1

    return L_matrix, U_matrix


def forward_substitution(L_matrix, B_matrix):
    # Forward Substitution
    for i in range(1, n):
        sum = B_matrix[i]
        for j in range(i):
            sum -= L_matrix[i][j] * B_matrix[j]
        B_matrix[i] = sum


def back_substitution(U_matrix, B_matrix):
    # Back Substitution
    X_matrix = np.zeros([n])
    X_matrix[n - 1] = B_matrix[n - 1] / U_matrix[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += U_matrix[i][j] * X_matrix[j]

        X_matrix[i] = (B_matrix[i] - sum) / U_matrix[i][i]

    return X_matrix


if __name__ == "__main__":
    A_matrix, B_matrix, n = take_input()
    L_matrix, U_matrix = constitute_LU(A_matrix, n)
    fp = open("out1.txt", "w")
    printMatrix(L_matrix, n, fp)
    printMatrix(U_matrix, n, fp)
    hasSolution(U_matrix, n, fp)
    forward_substitution(L_matrix, B_matrix)
    printArray(B_matrix, n, fp)
    X_matrix = back_substitution(U_matrix, B_matrix)
    printArray(X_matrix, n, fp, newline=False)
    fp.close()
