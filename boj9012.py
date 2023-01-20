import warnings
warnings.filterwarnings("ignore")

for _ in range(int(input())):
    try:
        eval(input())
    except SyntaxError:
        print('NO')
    except TypeError:
        print('YES')
    else:
        print('YES')
