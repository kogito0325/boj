def main():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(func(a, b))

def func(a, n):
    a = int(str(a)[-1])
    nstr = '111124863971464655556666793184269191'
    if a == 0:
        return '10'
    else:
        return nstr[(a - 1) * 4 : a * 4][n % 4 - 1]

if __name__ == '__main__':
    main()
