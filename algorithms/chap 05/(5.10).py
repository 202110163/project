def multiply(A, B, C):
    n = len(A)
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

C = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

multiply(A, B, C)
for row in C:
    print(row)
