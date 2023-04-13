num = int(input())

scores = [i for i in map(int, input().split())]

result = []

for n in scores:
    result.append(n / max(scores) * 100)

num = 0
for i in result:
    num += i

print(num / len(result))
