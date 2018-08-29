# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

n = int(input())
a = list(map(int, input().split()))
swaps = 0

for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swaps += 1

print('Array is sorted in %s swaps.' % swaps)
print('First Element: %s' % a[0])
print('Last Element: %s' % a[-1])
