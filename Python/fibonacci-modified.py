# https://www.hackerrank.com/challenges/fibonacci-modified/problem

t1, t2, n = map(int, input().split())
t = 0

for i in range(n - 2):
    t = t1 + t2 ** 2
    t1, t2 = t2, t

print(t)
