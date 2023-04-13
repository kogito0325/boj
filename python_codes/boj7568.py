people = []
num = int(input())
people_rank = [0 for _ in range(num)]

for _ in range(num):
    weight, height = map(int, input().split())
    people.append((weight, height))

rate = 1
for i, p in enumerate(people):
    bigger_count = 0
    for j in range(num):
        if people[j][0] > p[0] and people[j][1] > p[1]:
            bigger_count +=1
    people_rank[i] = rate + bigger_count

print(*people_rank)