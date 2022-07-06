# 나의 코드
num, base = map(int, input().strip().split(' '))
num = str(num)
answer = 0
for n in range(len(num)):
    answer += int(num[n])*(base**(len(num)-n-1))
print(answer)


# 앞으로 가야할 코드 방향
## 3212를 5진법으로 표현
num = '3212'
base = 5

answer = 0
for idx, number in enumerate(num[::-1]):
    print(idx, number)
    answer += int(number) * (base ** idx)
    
# 3212가 7진법일 때, 10진법으로 표현
num = '3212'
base = 7
answer = int(num, base)
print(answer)