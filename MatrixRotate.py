def rotate(m):
    A=m[::-1]
    for i in range(len(A)):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    return A
m =[[1,2,3],[4,5,6],[7,8,9]]
print(rotate(m))
