fir, sec, thi = map(int, input().split())

if fir == sec == thi:
    print(10000 + fir * 1000)
elif fir == sec or sec == thi or thi == fir:
    if fir in (sec, thi):
        print(1000 + fir * 100)
    else:
        print(1000 + sec * 100)
else:
    print(max(fir, sec, thi) * 100)