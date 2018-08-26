# https://www.hackerrank.com/challenges/sherlock-and-pairs/problem

t = int(input())

for _ in range(t):
    n = int(input())
    a = map(int, input().split())

    m = {}
    for i in a:
        if i not in m:
            m[i] = 0
        m[i] += 1

    print(sum(m[x] * (m[x] - 1) for x in m if m[x] > 1))
