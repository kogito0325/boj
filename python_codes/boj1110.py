s = input()
moto = int(s)
cnt = 0
while True:
    cnt += 1
    s = '0' + s if len(s) == 1 else s
    tmp_s = s[1] + str(int(s[0]) + int(s[1]))[-1]
    if int(tmp_s) == moto:
        break
    s = tmp_s
print(cnt)
