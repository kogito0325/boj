import sys
input = sys.stdin.readline
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


def numeral_average(iterable:list, n):
    return round(sum(iterable) / n)

def middle_value(iterable:list, n):
    return sorted(iterable)[int((n+1)/2-1)]

def most_prequency(iterable:list):
    ndic = {}
    ndic_values = []
    for i in iterable:
        if i not in ndic:
            ndic[i] = 1
        else:
            ndic[i] += 1
    mx_value = max(ndic.values())
    for i in ndic:
        if ndic[i] == mx_value:
            ndic_values.append(i)
    
    if len(ndic_values) > 1:
        return sorted(ndic_values)[1]
    else:
        return ndic_values[0]

def term(iterable:list):
    return max(iterable) - min(iterable)

def main():
    num_list = []
    n = int(input())

    for _ in range(n):
        num_list.append(int(input()))
    
    print(numeral_average(num_list, n))
    print(middle_value(num_list, n))
    print(most_prequency(num_list))
    print(term(num_list))

if __name__ == "__main__":
    main()