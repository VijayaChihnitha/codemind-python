N = int(input())
numbers = list(map(int, input().split()))

count = 0
for i in range(1, N - 1):
    if (numbers[i - 1] % 2 == 0 and numbers[i + 1] % 2 == 1) or (numbers[i - 1] % 2 == 1 and numbers[i + 1] % 2 == 0):
        count += 1

print(count)