# https://www.hackerrank.com/challenges/coin-change/problem

n, m = map(int, input().split())
coins = list(map(int, input().split()))
memo = [0] * (n + 1)
memo[0] = 1

for coin in coins:
    for change_ind in range(coin, n + 1):
        memo[change_ind] += memo[change_ind - coin]

print(memo[n])
