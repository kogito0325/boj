import sys

ndic = dict()
for _ in range(int(input())):
    if (n := int(sys.stdin.readline())) not in ndic:
        ndic[n] = 1
    else:
        ndic[n] += 1
    
for k in sorted(ndic):
    for i in range(ndic[k]):
        print(k) 