word_dic = {}

for i in input().upper():
    if i in word_dic:
        word_dic[i] += 1
    else:
        word_dic[i] = 0

count = 0
top = ''

for i in word_dic:
    if word_dic[i] == max(word_dic.values()):
        count += 1
        top = i

print('?' if count >= 2 else top)
