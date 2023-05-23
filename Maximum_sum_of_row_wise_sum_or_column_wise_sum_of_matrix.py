N, M = map(int, input().split())

# Create an empty matrix
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

max_row_sum = 0
max_col_sum = 0

# Calculate maximum row sum
for i in range(N):
    row_sum = sum(A[i])
    if row_sum > max_row_sum:
        max_row_sum = row_sum

# Calculate maximum column sum
for j in range(M):
    col_sum = sum(A[i][j] for i in range(N))
    if col_sum > max_col_sum:
        max_col_sum = col_sum

# Get the maximum sum
max_sum = max(max_row_sum, max_col_sum)

# Output the result
print(max_sum)