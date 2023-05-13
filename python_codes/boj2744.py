temp = ""
for c in input():
    if c in "abcdefghijklmnopqrstuvwxyz":
        temp += c.upper()
    else:
        temp += c.lower()
print(temp)