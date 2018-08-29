# https://www.hackerrank.com/challenges/two-strings/problem

p = int(input())

for _ in range(p):
    s1 = set(input())
    s2 = set(input())

    print('YES' if s1.intersection(s2) else 'NO')
