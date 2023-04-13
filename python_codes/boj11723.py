import sys
input = sys.stdin.readline

s = set([])
for _ in range(int(input())):
    try:
        _input = input()
        cmd, n = _input.split()
        n = int(n)
    except:
        cmd = _input.strip()
    if cmd == 'add':
        s.add(n)
    elif cmd == 'remove':
        if n in s:
            s.remove(n)
    elif cmd == 'check':
        print(1 if n in s else 0)
    elif cmd == 'toggle':
        if n in s:
            s.remove(n)
        else:
            s.add(n)
    elif cmd == 'all':
        s = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    elif cmd == 'empty':
        s.clear()