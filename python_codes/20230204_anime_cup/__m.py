import sys

def process_query(iterable:list, query:list):
    sequence = iterable[query[1]-1:query[2]]
    if query[0] == 1:
        for i in range(query[1]-1, query[2]):
            iterable[i] = min(iterable[i], query[3])
    elif query[0] == 2:
        for i in range(query[1]-1, query[2]):
            iterable[i] = max(iterable[i], query[3])
    elif query[0] == 3:
        for i in range(query[1]-1, query[2]):
            iterable[i] = iterable[i] + query[3]
    elif query[0] == 4:
        print(min(sequence))
    elif query[0] == 5:
        print(max(sequence))
    elif query[0] == 6:
        print(sum(sequence))
    return iterable


input()
numbers = list(map(int, input().split()))

for _ in range(int(input())):
    numbers = process_query(numbers, list(map(int, sys.stdin.readline().split())))


'''
3
20 10 2
6
2 1 3 7     # 20 10 7
4 2 3       # 7
1 1 2 4     # 4  4  7
5 2 2       # 4
3 1 1 5     # 9  4  7
6 1 2       # 13
'''