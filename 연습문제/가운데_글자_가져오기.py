def solution(s):
    # 글자수 저장
    l = len(s)
    # 글자수가 홀수라면,
    if l%2:
        answer = s[l//2]
    # 글자수가 짝수일경우
    else:
        answer = s[l//2-1:l//2+1]
    return answer