# 나의 코드
my_str = input().strip()

my_dic = {}
for number in my_str:
    try:
        my_dic[number] += 1
    except KeyError:
        my_dic[number] = 1
### 이 부분을 주석 부분처럼 수정
max_cnt = -1
for my in my_dic:
    if my_dic[my] > max_cnt:
        max_cnt = my_dic[my]
        
answer = []
for my in my_dic:
    if my_dic[my] == max_cnt:
        answer.append(my)
        
print("".join(sorted(answer)))

"""
max_cnt = -1
answer = []
for k, v in my_dic.items():
    if max_cnt < v:
        max_cnt = v
        answer = [k]
    elif v == max_cnt:
        stack.append(k)
stack.sort()
"""

# 앞으로 가야할 코드 방향
import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0