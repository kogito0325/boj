nums = [i for i in range(1, 30+1)]
for _ in range(28):
    nums.remove(int(input()))
print(*sorted(nums), sep='\n')