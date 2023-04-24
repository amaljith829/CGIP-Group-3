def rotate_clockwise(matrix):
    """
    Rotate a matrix clockwise by 90 degrees
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
    return matrix

# Get dimensions of the matrix from user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Get values of the matrix from user
matrix = []
print("Enter the values of the matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter the value at ({i}, {j}): "))
        row.append(value)
    matrix.append(row)

# Print the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Rotate the matrix clockwise
rotated_matrix = rotate_clockwise(matrix)

# Print the rotated matrix
print("Rotated Matrix:")
for row in rotated_matrix:
    print(row)

