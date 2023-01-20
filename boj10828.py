import sys

stack = list()

for _ in range(int(input())):
    answer = sys.stdin.readline().rstrip()
    if answer.startswith('push'):
        stack.append(int(answer.split()[-1]))
    elif answer == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop(-1))
    elif answer == 'size':
        print(len(stack))
    elif answer == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif answer == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])