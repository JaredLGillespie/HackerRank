# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem

n, k = map(int, input().split())
x = sorted(list(map(int, input().split())))
antennaes = 0
last_antennae = -float('inf')

i = 0
while i < n:
    if x[i] <= last_antennae + k:
        i += 1
        continue

    j = i
    while j < n and x[i] >= x[j] - k:
        j += 1

    antennaes += 1
    last_antennae = x[j - 1]

    if i == j:
        i += 1
    else:
        i = j

print(antennaes)
