def solution(n,a,b):
    answer = 1
    while True:
        # a와 b를 -1하고 난 몫이 같다면 같은 대전
        if (a-1)//2 == (b-1)//2:
            return answer
        # 아니라면 승리해서 다시 번호를 할당받으므로!
        else:
            a = (a+1)//2
            b = (b+1)//2
            answer += 1
            