import sys
num_range = int(input())
num_list = list(0 for _ in range(num_range))

for i in range(num_range):
    num_list[i] = int(sys.stdin.readline().rstrip())

print(*sorted(num_list), sep='\n')