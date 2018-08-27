# https://www.hackerrank.com/challenges/2d-array/problem

arr = [list(map(int, input().split())) for _ in range(6)]
max_sum = -float('inf')

for row in range(4):
    for col in range(4):
        max_sum = max(arr[row][col] + arr[row][col + 1] + arr[row][col + 2] +
                      arr[row + 1][col + 1] +
                      arr[row + 2][col] + arr[row + 2][col + 1] + arr[row + 2][col + 2],
                      max_sum)

print(max_sum)
