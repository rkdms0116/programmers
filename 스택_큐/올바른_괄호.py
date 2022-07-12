def solution(s):
    cnt = 0
    for q in s:
        if q == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
            break
    if cnt == 0:
        return True
    else:
        return False