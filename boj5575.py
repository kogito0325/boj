def count_time():
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    seconds = ((h2 * 60 + m2) * 60 + s2) - ((h1 * 60 + m1) * 60 + s1)
    s = seconds % 60
    seconds = seconds - seconds % 60
    m = (seconds % 3600) // 60
    seconds = seconds - (seconds % 3600) // 60
    h = seconds // 3600
    print(h, m, s)
    

for _ in range(3):
    count_time()