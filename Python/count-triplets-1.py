# https://www.hackerrank.com/challenges/count-triplets-1

from collections import defaultdict


n, r = map(int, input().split())
arr = list(map(int, input().split()))
m1, m2 = defaultdict(int), defaultdict(int)

triplets = 0

for i in reversed(arr):
    if (i * r) in m2:
        triplets += m2[i * r]

    if (i * r) in m1:
        m2[i] += m1[i * r]

    m1[i] += 1

print(triplets)
