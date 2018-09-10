# https://www.hackerrank.com/challenges/gem-stones/problem

n = int(input())
arr = [set(input()) for _ in range(n)]
sub = arr[0]

for a in arr:
    sub.intersection_update(a)

print(len(sub))
