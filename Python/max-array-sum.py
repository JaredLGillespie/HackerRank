# https://www.hackerrank.com/challenges/max-array-sum/problem

n = int(input())
arr = list(map(int, input().split()))
v = [0] * n

for i in range(n):
    if i < 2:
        v[i] = max(arr[i], 0)
        continue
    elif i == 2:
        v[i] = v[i - 2] + max(arr[i], 0)
        continue

    v[i] = max(v[i-2], v[i-3]) + max(arr[i], 0)

print(max(v[-1], v[-2]))
