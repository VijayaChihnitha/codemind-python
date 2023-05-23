N, M = map(int, input().split())

# Create an empty matrix
matrixA = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrixA.append(row)

max_row_sum = 0

# Calculate maximum row sum
for i in range(N):
    row_sum = sum(matrixA[i])
    if row_sum > max_row_sum:
        max_row_sum = row_sum

# Output the result
print(max_row_sum)