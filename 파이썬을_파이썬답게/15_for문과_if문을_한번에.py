# 나의 코드
def solution(mylist):
    answer = []
    for my in mylist:
        if not my%2:
            answer.append(my**2)
    return answer


# 앞으로 가야할 코드 방향
mylist = [3, 2, 6, 7]
answer = [number**2 for number in mylist if number % 2 == 0]