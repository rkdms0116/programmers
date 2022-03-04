from collections import deque
def solution(s):
    string = deque()
    
    for st in s:
        # string이 비어있으면 넣어주고
        if len(string) == 0:
            string.append(st)
        # 비어있지 않으면
        else:
            # string list의 마지막과 비교
            if st == string[-1]:
                # 같으면 list 마지막 제거
                string.pop()
            else:
                # 아니면 append
                string.append(st)
                
    if string:
        answer = 0
    else:
        answer = 1

    return answer