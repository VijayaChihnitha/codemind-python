N = int(input())

# Read matrix A
matrixA = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrixA.append(row)

# Read matrix B
matrixB = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrixB.append(row)

# Initialize the difference matrix
diffMatrix = []

# Compute the absolute difference matrix
for i in range(N):
    diffRow = []
    for j in range(N):
        diff = abs(matrixA[i][j] - matrixB[i][j])
        diffRow.append(diff)
    diffMatrix.append(diffRow)

# Print the difference matrix
for row in diffMatrix:
    print(' '.join(map(str,row)))