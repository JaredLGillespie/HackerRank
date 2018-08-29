# https://www.hackerrank.com/challenges/frequency-queries/problem

from collections import defaultdict, deque


q = int(input())
arr = defaultdict(int)
out = deque()
freq = defaultdict(set)

for _ in range(q):
    o, n = map(int, input().split())

    if o == 1:
        v = arr[n]
        arr[n] = v + 1

        if n in freq[v]:
            freq[v].remove(n)

        freq[v + 1].add(n)

    elif o == 2:
        v = arr[n]

        if v > 0:
            v = arr[n]
            arr[n] = v - 1

            if n in freq[v]:
                freq[v].remove(n)

            freq[v - 1].add(n)
    else:
        if freq[n]:
            out.append(1)
        else:
            out.append(0)

for i in out:
    print(i)
