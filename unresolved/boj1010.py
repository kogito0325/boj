# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     a, b = max(a, b), min(a, b)
#     print(sum(i for i in range(a)) - sum(i for i in range(b)) + 1 )

res = 1
for i in range(1, int(input())+1):
    res *= i
print(res)

'''
1 1
1

1 2
2

2 2
1

1 3
3

2 3
2 1

3 3
1

1 4
4

2 4
3 2 1

3 4
2 1 1

4 4
1

1 5
5

2 5
4 3 2 1

3 5
3 2 1 2 1 1

4 5
2 1 1 1

5 5
1

1 6
6

2 6
5 4 3 2 1

3 6
4 3 2 1 3 2 1 2 1 1
4 6
3 2 1 2 1 1 1

'''
