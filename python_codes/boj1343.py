answer = input()
answer += '.'
string = ''
cnt = 1
for i, c in enumerate(answer):
    if c == '.':
        string += '.'
        continue
    if answer[i+1] == '.':
        if cnt % 2:
            print(-1)
            exit()
        string += 'A' * ((cnt // 4) * 4)
        cnt %= 4
        string += 'B' * cnt
        cnt = 1
    else:
        cnt += 1
print(string[:-1])