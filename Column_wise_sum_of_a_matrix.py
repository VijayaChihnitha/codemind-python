n, m = map(int, input().split())

# Read the elements of the matrix
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Initialize a list to store the column sums
column_sums = [0] * m

# Calculate the sum of individual columns
for j in range(m):
    for i in range(n):
        column_sums[j] += matrix[i][j]

# Print the sum of individual columns
print(' '.join(map(str,column_sums)))