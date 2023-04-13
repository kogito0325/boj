n = int(input())
numbers = [_ for _ in range(n, 0, -1)]
stack = []
process = []
possible = True

for i in range(n):
    answer = int(input())
    while possible:
        if answer not in stack:
            stack.append(numbers.pop())
            process.append('+')
        else:
            if answer != stack[-1]:
                possible = False
            else:
                stack.pop()
                process.append('-')
                break
if possible:
    for p in process: print(p)
else:
    print('NO')
