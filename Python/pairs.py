# https://www.hackerrank.com/challenges/pairs/problem

n, k = map(int, input().split())
arr = list(map(int, input().split()))
memo = set()
count = 0

for v in arr:
    if k + v in memo:
        count += 1
    if v - k in memo:
        count += 1

    memo.add(v)
print(count)
