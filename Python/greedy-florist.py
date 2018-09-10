# https://www.hackerrank.com/challenges/greedy-florist/problem

n, k = map(int, input().split())
flowers = sorted(list(map(int, input().split())))
cost = 0

for i in range(n - 1, -1, -1):
    cost += flowers[i] * (((n - i - 1) // k) + 1)
print(cost)
