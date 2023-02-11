while True:
    if (s:=input()) == '.':
        break
    stack = []
    valanced = True
    for i in s:
        if i in ('[', '('):
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                valanced = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                valanced = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if valanced == True and not stack:
        print('yes')
    else:
        print('no')    