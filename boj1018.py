import sys 

correct1 = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

correct2 = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

height, width = map(int, input().split())

chess = [sys.stdin.readline().rstrip() for _ in range(height)]

def find_answer(correct : list):
    cnt = 64
    for x_offset in range(width - 7):
        for y_offset in range(height - 7):
            tmp = 0
            for y in range(8):
                for x in range(8):
                    if chess[y + y_offset][x + x_offset] == correct[y][x]:
                        tmp += 1
            cnt = min(tmp, cnt)
    return cnt

print(min(find_answer(correct1), find_answer(correct2)))