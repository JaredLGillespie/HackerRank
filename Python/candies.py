# https://www.hackerrank.com/challenges/candies/problem

n = int(input())
arr = [int(input()) for _ in range(n)]
candies = [1] * n

for i in range(1, n):
    if arr[i - 1] < arr[i]:
        candies[i] = candies[i - 1] + 1

for i in range(n - 2, -1, -1):
    if arr[i + 1] < arr[i]:
        if i - 1 >= 0 and arr[i - 1] < arr[i]:
            candies[i] = max(candies[i + 1], candies[i - 1]) + 1
        else:
            candies[i] = candies[i + 1] + 1

print(sum(candies))
