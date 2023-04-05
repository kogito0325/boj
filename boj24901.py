bins = [0] * 11
for i in range(0, 11):
    bins[i] = bin(i)[2:]

print(bins)
n = int(input())
print(''.join(bins[:n+1]))