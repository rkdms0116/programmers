def solution(p):
    answer = ''
    if not(p):
        return p

    if check(p):
        return p

    [u, v] = sep(p)

    if check(u):
        return u + solution(v)
    else:
        answer += '('
        for i in range(len(u)-2,0,-1):
            answer += u[i]
        answer += ')'
        
    return answer
        
def check(p):
    x = y = 0
    for i in range(len(p)):
        if i == 0:
            if p[i] == '(':
                x += 1
            else:
                return False
        else:
            if y == x:
                return False
            if p[i] == '(':
                x += 1
            else:
                y += 1
            if y == x and x+y == len(p):
                return True
    else:
        return True
    
def sep(p):
    x = y = 0
    for i in range(len(p)):
        if p[i] == '(':
            x += 1
        else:
            y += 1
        if x==y:
            u = p[:i+1]
            v = p[i+1:]
            return [u,v]
print(check("())(()"))
print(solution("()))((()"))