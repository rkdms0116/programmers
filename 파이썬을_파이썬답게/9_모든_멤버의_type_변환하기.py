# 나의 코드
def solution(mylist):
    answer = [int(my) for my in mylist]
    return answer


# 앞으로 가야할 코드 방향
list1 = ['1', '100', '33']
list2 = list(map(int, list1))
# list2 = list(map(int, *list1))
# unpack 해서 틀렸...