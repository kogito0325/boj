import sys

range_num = int(input())
word_dic = dict()
result_list = list()

for i in range(range_num):
    word = sys.stdin.readline().rstrip()
    if word not in word_dic:
        word_dic[word] = len(word)

for n in range(1, max(word_dic.values()) + 1):
    temp_list = list()
    for k in word_dic:
        if word_dic[k] == n:
            temp_list.append(k)
    result_list.append(sorted(temp_list))

# print('------------------------------')

for l in result_list:
    for e in l:
        print(e)
