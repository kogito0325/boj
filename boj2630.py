n = int(input())
matrix = [0 for _ in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input().split()))

b_cnt = 0
w_cnt = 0
words = [2 ** i for i in range(7,-1,-1)]

def div_con(word:int, matrix:list, n:int):
    global b_cnt, w_cnt
    for y in range(0, n, word):
        for x in range(0, n, word):
            stack = 0
            for my in range(word):
                if 1 not in matrix[y+my][x:x+word] and 2 not in matrix[y+my][x:x+word]:
                    stack += 1
            if stack == word:
                w_cnt += 1
                for i in range(word):
                    matrix[y+i][x:x+word] = [2] * word
            stack = 0
            for my in range(word):
                if 0 not in matrix[y+my][x:x+word] and 2 not in matrix[y+my][x:x+word]:
                    stack += 1
            if stack == word:
                b_cnt += 1
                for i in range(word):
                    matrix[y+i][x:x+word] = [2] * word
    print(*matrix, sep='\n')
    print(w_cnt, b_cnt)

for w in words[words.index(n):]:
    div_con(w, matrix, n)

print(w_cnt)
print(b_cnt)