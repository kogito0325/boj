bottles, tar = map(int, input().split())

sup = 0
while bin(bottles).count('1') > tar:
    sup += 1
    bottles += 1

print(sup)