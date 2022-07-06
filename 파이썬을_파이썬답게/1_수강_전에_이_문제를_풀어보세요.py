# 나의 코드
def solution(mylist):
    answer = []
    for my in mylist:
        answer.append(len(my))
    return answer


# 앞으로 가야할 코드 방향
def solution(mylist):
    return list(map(len, mylist))