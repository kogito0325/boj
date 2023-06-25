for _ in range(3):
	points = input()
    if points.count('1') == 4:
        print('E')
        continue
    print("ABCD"[points.count('0') - 1])
