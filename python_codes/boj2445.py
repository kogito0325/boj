n=int(input())
r=range
p=print
for i in r(1,n+1):p('*'*i+' '*(n-i)*2+'*'*i)
for i in r(n-1, 0, -1):p('*'*i+' '*(n-i)*2+'*'*i)