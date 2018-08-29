# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

q = int(input())
fact_mem = {}


def factorial(x):
    if x in fact_mem:
        return fact_mem[x]

    v = factorial(x - 1) * x if x > 1 else 1
    fact_mem[x] = v
    return v


for _ in range(q):
    s = input()
    m = {}
    anagrams = 0

    for window_size in range(1, len(s)):
        for offset in range(len(s) - window_size + 1):
            v = tuple(sorted(s[offset:offset+window_size]))
            if v not in m:
                m[v] = 0
            m[v] += 1

    for window, frequency in m.items():
        if frequency > 1:
            anagrams += factorial(frequency) // (factorial(frequency - 2) * 2)

    print(anagrams)
