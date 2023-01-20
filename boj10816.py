import sys

sys.stdin.readline()
ndic = dict()
for n in map(int, sys.stdin.readline().split()):
    if n not in ndic:
        ndic[n] = 1
    else:
        ndic[n] += 1
sys.stdin.readline()
for k in map(int, sys.stdin.readline().split()):
    if k in ndic:
        print(ndic[k], end=' ')
    else:
        print(0, end=' ')
