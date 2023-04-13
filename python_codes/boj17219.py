n, m = map(int, input().split())

account_dict = {}
for _ in range(n):
    id_, pw = input().split()
    account_dict[id_] = pw

for _ in range(m):
    print(account_dict[input()])
