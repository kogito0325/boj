n = int(input())
nums = [i for i in range(n)]
empty = []
matrix = [0] * n

for i in range(n):
    matrix[i] = input()
    if 'W' in matrix[i] and list(matrix[i]).index('W') in nums:
        nums.remove(list(matrix[i]).index('W'))
        continue
    empty.append(i)

for i in range(len(empty)):
    matrix[empty[i]] = '.' * (nums[i]) + 'W' + '.' * (n - nums[i] - 1)

print(*matrix, sep='\n')
