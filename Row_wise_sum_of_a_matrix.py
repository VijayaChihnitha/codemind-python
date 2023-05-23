N, M = map(int, input().split())

matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

row_sums = []
for row in matrix:
    row_sum = sum(row)
    row_sums.append(row_sum)

print(' '.join(map(str,row_sums)))