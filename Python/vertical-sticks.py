# https://www.hackerrank.com/challenges/vertical-sticks/problem

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    y = sorted(map(int, input().split()))
    k = [n + 1] * n

    for i in range(1, n):
        if y[i] == y[i - 1]:
            k[i] = k[i - 1]
        else:
            k[i] = n - i + 1

    ans = (n + 1) * sum(1 / k[i] for i in range(n))
    print('%.2f' % ans)
