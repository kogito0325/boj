from collections import deque

for _ in range(int(input())):
    cmd = input()
    input()
    queue = []
    try:
        queue = list(map(int, input()[1:-1].split(',')))
    except ValueError:
        pass
    queue_s = deque(queue)
    rvs = False
    empty = False
    for s in cmd:
        if s == 'R':
            rvs = not rvs
        else:
            if not queue_s:
                empty = True
                break
            if rvs:
                queue_s.pop()
            else:
                queue_s.popleft()
    if empty:
        print('error')
    else:
        print('[', end='')
        if rvs:
            print(*reversed(queue_s), sep=',', end='')
        else:
            print(*queue_s, sep=',', end='')
        print(']')


