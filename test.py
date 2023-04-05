import random

while True:
    a, b = 1, int(input())
    cnt = 1
    while random.randint(a, b) != b:
        cnt += 1
        print(f'이론상 확률: {100 / b:.16f} / 실제 확률: {100 / cnt:.16f}')
    print('-----------------------------------')