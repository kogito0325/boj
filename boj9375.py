for _ in range(int(input())):
    clothe_dict = dict()
    n = int(input())
    if not n:
        print(0)
        continue
    for i in range(n):
        c, t = input().split()
        if t not in clothe_dict:
            clothe_dict[t] = 1
        else:
            clothe_dict[t] += 1

    way = 1
    if len(clothe_dict) == 1:
        print(clothe_dict[t])
        continue
    for s in clothe_dict:
        clothe_dict[s] += 1
        way *= clothe_dict[s]
    print(way - 1)