# 나의 코드
from itertools import permutations

def solution(mylist):
    answer = []
    my_per = permutations(mylist, len(mylist))
    for my in my_per:
        answer.append(my)
    return sorted(answer)


# 앞으로 가야할 코드 방향
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기