# https://www.hackerrank.com/challenges/bday-gift/problem

n = int(input())
s = sum(int(input()) for _ in range(n))
print('%.1f' % (s / 2))
