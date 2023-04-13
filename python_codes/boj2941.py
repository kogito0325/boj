cro_al = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] + [chr(i) for i in range(97, 123)]
word = input()
count = 0
while True:
    for c in cro_al:
        if word.startswith(c):
            count += 1
            word = word[len(c):]
            break
    if not len(word):
        break
print(count)