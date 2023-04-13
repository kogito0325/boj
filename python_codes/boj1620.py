import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemons = [' ' for _ in range(n)]
for i in range(n):
    pokemons[i] = input().strip()

for _ in range(m):
    a = input().strip()
    try:
        a = int(a)
        print(pokemons[a - 1])
    except:
        print(pokemons.index(a) + 1)
