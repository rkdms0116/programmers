from collections import deque
def solution(s):
    answer = 0
    # 문자열 s를 list로 변환
    parentheses = list(s)
    for _ in range(len(parentheses)):
        stack = deque()
        
        for p in parentheses:
            if p==')' and stack and stack[-1] == '(':
                stack.pop()
            elif p=='}' and stack and stack[-1] == '{':
                stack.pop()
            elif p==']' and stack and stack[-1] == '[':
                stack.pop()
            # 열린 괄호라면 Stack에 append
            else:
                stack.append(p)
        # for문을 다 돌고 나서 stack이 비어있는지 확인
        if not(stack):
            answer += 1
        # 문자열 s를 왼쪽으로 한칸씩 회전
        parentheses.append(parentheses.popleft())
    return answer            

print(solution("[](){}"))