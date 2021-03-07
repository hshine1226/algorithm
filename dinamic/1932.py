n = eval(input())

triangle = list()
dp = [[0 for i in range(n)]] * n

for i in range(n):
    num = list(map(int, input().split()))
    triangle.append(num)

k = 0
for i in range(n):
    if k == 0:
        dp[0][0] = triangle[i][0]
    for j in range(k):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    k += 1

print(dp)
