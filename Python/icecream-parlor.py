# https://www.hackerrank.com/challenges/icecream-parlor/problem

t = int(input())

for _ in range(t):
    m = int(input())
    n = int(input())
    cost = list(map(int, input().split()))
    memo = {}

    for i, c in enumerate(cost):
        if (m - c) in memo:
            print('%s %s' % (memo[m - c], i + 1))
            break
        memo[c] = i + 1
