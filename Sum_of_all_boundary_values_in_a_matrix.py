def sum_boundary_values(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    boundary_sum = 0

    for i in range(rows):
        for j in range(cols):
            # Check if the current element is on the boundary
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                boundary_sum += matrix[i][j]

    return boundary_sum

# Get the matrix size from the user
N, M = map(int, input().split())

# Initialize an empty matrix
matrixA = []

# Get the matrix elements from the user
for _ in range(N):
    row_elements = list(map(int, input().split()))
    matrixA.append(row_elements)

# Calculate the sum of boundary values
boundary_sum = sum_boundary_values(matrixA)

# Display the result
print(boundary_sum)