# for _ in sorted(map(int, input().split())):
#     print(_, end=' ')

print(*sorted(input().split(),key=int))