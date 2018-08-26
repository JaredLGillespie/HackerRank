# https://www.hackerrank.com/challenges/picking-cards/problem

t = int(input())

for _ in range(t):
    n = int(input())
    c = sorted(map(int, input().strip().split()), reverse=True)

    ans = 1
    for i, c in enumerate(c):
        val = n - c
        if val <= 0:
            print(0)
            break

        ans = (ans * (val - i)) % 1000000007
    else:
        print(ans % 1000000007)
