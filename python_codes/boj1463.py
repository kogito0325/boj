dp = [0, 1, 1] + [0] * (n:=int(input()))

for i in range(3, n):
    dp[i] = dp[i-1] + 1

    if not (i + 1) % 2:
        dp[i] = min(dp[i], dp[int((i+1)/2)-1] + 1)
    if not (i + 1) % 3:
        dp[i] = min(dp[i], dp[int((i+1)/3)-1] + 1)

print(dp[n-1])
