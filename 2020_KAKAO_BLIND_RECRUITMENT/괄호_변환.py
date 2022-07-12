def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if p == '':
        return ''
    else:
        # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
        u, v = sep(p)
        # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
        if check(u):
            # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
            return u + solution(v)
        # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
        else:
            # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
            # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
            # 4-3. ')'를 다시 붙입니다. 
            answer = '(' + solution(v) + ')'
        
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        for i in u[1:len(u)-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    # 4-5. 생성된 문자열을 반환합니다.      
    return answer

# 문자열을 두 균형잡힌 문자열 u, v로 분리하는 함수
def sep(questions):
    cut = 0
    for idx in range(len(questions)):
        if questions[idx] == '(':
            cut += 1
        else:
            cut -= 1
        if idx > 0 and cut == 0:
            u = questions[:idx+1]
            v = questions[idx+1:]
            break
    return u, v

# 문자열이 올바른 문자열인지 확인하는 함수
def check(words):
    idx = cnt = 0
    while idx < len(words):
        if words[idx] == '(':
            cnt += 1
        else:
            cnt -= 1
        idx += 1
        
        if cnt < 0:
            return False
    return True


'''
def solution(p):
    answer = ''
    if not(p):
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


print("hello"[2:])
print("hello"[:2])
'''