h, m = map(int, input().split())
fixed = h * 60 + m - 45
print(f'{23 if fixed // 60 < 0 else fixed // 60} {fixed % 60}')
