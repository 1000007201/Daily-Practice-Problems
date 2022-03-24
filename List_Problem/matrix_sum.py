
mat1 = [[1, 2, 3],
        [4, 5, 7],
        [8, 6, 2]]

mat2 = [[1, 2, 3],
        [4, 5, 7],
        [8, 6, 2]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]


for i in range(len(mat1)):
    for j in range(len(mat2)):
        result[i][j] = mat1[i][j] + mat2[i][j]

print(result)