def binary_search(iter, start, end, target):
    # input()
    middle = (start + end) // 2
    count = 0
    for n in iter:
        count += n // middle
    if count >= target:
        # print(f'{middle} : {count} >= {target}')
        if start == middle:
            return middle
        return binary_search(iter, middle, end, target)
    # print(f'{middle} : {count} < {target}')
    return binary_search(iter, start, middle, target)

n, k = map(int, input().split())

nlist = []
for _ in range(n):
    nlist.append(int(input()))

std = max(nlist)

print(binary_search(nlist, 1, std, k))