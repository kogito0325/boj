num = int(input())

string = input()
whole = 0
for i in range(num):
    whole += ((ord(string[i]) - 96) * 31 ** i)

print(whole % 1234567891)