import sys

deque = list()

for _ in range(int(input())):
    answer = sys.stdin.readline().rstrip()
    if answer.startswith('push_front'):
        deque.insert(0, (int(answer.split()[-1])))
    elif answer.startswith('push_back'):
        deque.append(int(answer.split()[-1]))
    elif answer == 'pop_front':
        if not deque:
            print(-1)
        else:
            print(deque.pop(0))
    elif answer == 'pop_back':
        if not deque:
            print(-1)
        else:
            print(deque.pop(-1))
    elif answer == 'size':
        print(len(deque))
    elif answer == 'empty':
        if not deque:
            print(1)
        else:
            print(0)
    elif answer == 'front':
        if not deque:
            print(-1)
        else:
            print(deque[0])
    elif answer == 'back':
        if not deque:
            print(-1)
        else:
            print(deque[-1])