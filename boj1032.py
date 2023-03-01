string = ""
for _ in range(int(input())):
    if not string:
        string = input()
        continue
    temp_string = ''
    for i in range(len(s:=input())):
        if string[i] != s[i]:
            temp_string += '?'
        else:
            temp_string += string[i]
    string = temp_string
print(string)    