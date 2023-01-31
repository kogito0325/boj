import sys
for _ in range(3):
    sum_ = 0
    for i in range(int(input())):
        sum_ += int(sys.stdin.readline())
    print('+' if sum_ > 0 else '-' if sum_ < 0 else 0)