moto_s = input()
s = 'z' * 50
for i in range(1, len(moto_s)-1):
    for j in range(i+1, len(moto_s)):
        a = moto_s[:i][::-1]
        b = moto_s[i:j][::-1]
        c = moto_s[j:][::-1]
        temp_s = a + b + c
        if temp_s <= s:
            s = temp_s
print(s)
