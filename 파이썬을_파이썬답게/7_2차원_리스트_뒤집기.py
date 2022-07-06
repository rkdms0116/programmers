# 나의 코드
import enum


def solution(mylist):
    answer = []
    for i in range(len(mylist)):
        temp = list()
        for my in mylist:
            temp.append(my[i])
        answer.append(temp)
    return answer


# 앞으로 가야할 코드 방향
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))
print(new_list)

mylist = [1, 2, 3]
new_list = [40, 50, 60]
for i in zip(mylist, new_list):
    print (i)

for idx, my in enumerate(new_list):
    print(idx, my)