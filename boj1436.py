n = 665
target = int(input())

while True:
    n += 1
    if '666' in str(n):
        target -= 1
    if not target:
        break
print(n)