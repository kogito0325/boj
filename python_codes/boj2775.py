def calculate(iterable:list, floor:int):
    if not floor:
        return iterable
    else:
        temp_iterable = [0 for _ in range(14)]
        for i in range(14):
            temp_iterable[i] = sum(iterable[:i+1])
        return calculate(temp_iterable, floor - 1)


for _ in range(int(input())):
    floor = int(input())
    num = int(input())
    num_list = [i for i in range(1, 15)]
    print(calculate(num_list, floor)[num-1])
