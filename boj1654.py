def binary_search(iter, start, end, target):
    if (start + end) % 2 == 0:
        middle = (start + end) // 2
    else:
        middle = (start + end) // 2 + 1
    count = 0
    for n in iter:
        count += n // middle

    if count >= target:
        if middle == start:
            return middle
        return binary_search(iter, middle, end, target)
    return binary_search(iter, start, middle -1 , target)

n, k = map(int, input().split())

nlist = []
for _ in range(n):
    nlist.append(int(input()))

std = max(nlist)

print(binary_search(nlist, 0, std, k))