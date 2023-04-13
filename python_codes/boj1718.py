alphabets = list(chr(a) for a in range(97, 123))
sentence = input()
cipher = input()

for i, c in enumerate(sentence):
    if c == ' ':
        print(c, end='')
    else:
        print(alphabets[alphabets.index(c) - alphabets.index(cipher[i % len(cipher)]) - 1], end='')