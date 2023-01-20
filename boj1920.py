def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


num_range = int(input())
num_list = list(sorted(map(int, input().split())))

input()
for n in map(int, input().split()):
    print(binary_search(num_list, n, 0, num_range - 1))