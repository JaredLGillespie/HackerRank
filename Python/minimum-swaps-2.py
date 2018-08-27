# https://www.hackerrank.com/challenges/minimum-swaps-2/problem

n = int(input())
arr = list(map(int, input().split()))
swaps = 0

for i in range(0, n - 1):
    while arr[i] != i + 1:
        t = arr[arr[i] - 1]
        arr[arr[i] - 1] = arr[i]
        arr[i] = t
        swaps += 1

print(swaps)
