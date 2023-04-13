'''
1 1 1 2 2 3 4 5 7 9 12
'''

dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for _ in range(int(input())):
    for i in range(10, n:=int(input())):
        if i >= len(dp):
            dp += [0]
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[n-1])
