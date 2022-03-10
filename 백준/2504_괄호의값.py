from collections import deque

test = input()
stack = deque()
answer = []
result = 0
for n in range(len(test)):

    if n != 0 and not(stack):
        temp = 0
        for a in answer[::-1]:
            
            if a == '3*':
                temp *= 3
            elif a == '2*':
                temp *= 2
            else:
                temp += int(a)
        result += temp
        answer = []

    if test[n] == '(':
        stack.append('(')
        if n < len(test)-1 and test[n+1] == ')':
            answer.append('2')
        else:
            answer.append('2*')
    elif test[n] == '[':
        stack.append('[')
        if n < len(test)-1 and test[n+1] == ']':
            answer.append('3')
        else:
            answer.append('3*')
    elif test[n] == ')':
        if stack and stack[-1] == '(':
            stack.pop()
        elif stack:
            stack.append(')')
        else:
            result = 0 
            break
    elif test[n] == ']':
        if stack and stack[-1] == '[':
            stack.pop()
        elif stack:
            stack.append(']')
        else:
            result = 0 
            break

print(answer)

if stack:
    result = 0

else:
    temp = 0
    for a in answer[::-1]:

        if a == '3*':
            temp *= 3
        elif a == '2*':
            temp *= 2
        else:
            temp += int(a)
    result += temp

print(result)
