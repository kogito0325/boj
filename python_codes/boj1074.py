def div_con(word:int, std:int, y_mid, x_mid, y, x):
    if word == 1:
        return std
    w = word**2 // 4
    dw = word//4
    if y >= y_mid and x >= x_mid:
        y_mid += dw
        x_mid += dw
        return div_con(word // 2, std + w*3, y_mid, x_mid, y, x)
    if y >= y_mid and x < x_mid:
        y_mid += dw
        x_mid -= dw
        return div_con(word // 2, std + w*2, y_mid, x_mid, y, x)
    if y < y_mid and x >= x_mid:
        y_mid -= dw
        x_mid += dw
        return div_con(word // 2, std + w*1, y_mid, x_mid, y, x)
    if y < y_mid and x < x_mid:
        y_mid -= dw
        x_mid -= dw
        return div_con(word // 2, std + w*0, y_mid, x_mid, y, x)

n, y, x = map(int ,input().split())
n = 2**n
print(div_con(n, 0, n//2, n//2, y, x))
