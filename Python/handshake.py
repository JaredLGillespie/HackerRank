# https://www.hackerrank.com/challenges/handshake/problem

t = int(input())

for _ in range(t):
    n = int(input())
    print(n * (n - 1) // 2)
