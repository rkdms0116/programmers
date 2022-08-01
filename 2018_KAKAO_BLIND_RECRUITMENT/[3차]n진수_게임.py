# 16진수까지 만들 수 있는 함수
def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)
    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]

def solution(n, t, m, p):
    # 변환한 값을 numstr에 할당
    numstr = ''
    for i in range(0, m*t):
        numstr += convert(i, n)
    # 내가 볼 시작 index
    idx = p-1
    answer = ''
    while True:
        # 정답의 길이가 t면 break
        if len(answer) == t:
            return answer
        answer += str(numstr[idx])
        # 게임 참가 인원 수 만큼 index ++
        idx += m