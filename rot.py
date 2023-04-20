def rotate_clockwise(matrix):
    n = len(matrix)
    rotated_matrix = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n-i-1] = matrix[i][j]
    return rotated_matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated_matrix = rotate_clockwise(matrix)
print(rotated_matrix)

