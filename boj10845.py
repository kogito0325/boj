import sys

queue = list()

for _ in range(int(input())):
    answer = sys.stdin.readline().rstrip()
    if answer.startswith('push'):
        queue.append(int(answer.split()[-1]))
    elif answer == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    elif answer == 'size':
        print(len(queue))
    elif answer == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif answer == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif answer == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])