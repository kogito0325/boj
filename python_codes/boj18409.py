n = int(input())
cnt = 0
vowels = 'aiueo'
for c in input():
    if c in vowels:
        cnt += 1
print(cnt)