n, whole = map(int, input().split())

coins = [i for i in range(n)]
for i in range(n):
    coins[i] = int(input())

coins.sort(reverse=True)
cnt = 0
for k in coins:
    cnt += whole // k
    whole %= k

print(cnt)