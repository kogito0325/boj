def binary_search(iter:list, start, end, target):
    cut = (start + end) // 2
    count = 0
    temp_list = []
    for n in iter:
        if n >= cut:temp_list.append(n)
    for n in temp_list:
        count += n - cut

    if count >= target:
        if cut == end:
            return cut
        return binary_search(iter, cut + 1, end, target)
    return binary_search(iter, start, cut - 1, target)

a, b = map(int, input().split())

trees = [0 for _ in range(a)]
for i, n in enumerate(map(int, input().split())):
    trees[i] = n

std = max(trees)

print(binary_search(trees, 1, std, b))