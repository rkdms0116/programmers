# 나의 코드
def solution(mylist):
    answer = []
    for m in range(len(mylist)-1):
        answer.append(abs(mylist[m]-mylist[m+1]))
    return answer


# 앞으로 가야할 코드 방향
def solution(mylist):
    answer = []
    for my1, my2 in zip(mylist, mylist[1:]):
        answer.append(abs(my1-my2))
    return answer
