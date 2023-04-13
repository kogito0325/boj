cut, brands = map(int, input().split())
cut1 = cut
cost6 = 10000
cost1 = 10000
for _ in range(brands):
    temp_cost6, temp_cost1 = map(int, input().split())
    cost6 = min(cost6, temp_cost6)
    cost1 = min(cost1, temp_cost1)

cost = 0
cost += cut // 6 * cost6
cut %= 6
cost += min(cost6, cost1 * cut)
cost = min(cost, cost1 * cut1)

print(cost)