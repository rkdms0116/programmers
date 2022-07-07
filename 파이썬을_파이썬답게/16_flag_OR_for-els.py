# 나의 코드
flag = False
mul = 1
for _ in range(5):
    mul *= int(input())
    for m in range(1, mul+1):
        if m**2 == mul:
            flag = True
if flag:
    print("found")
else:
    print("not found")


# 앞으로 가야할 코드 방향
import math

if __name__ == '__main__':
    numbers = [int(input()) for _ in range(5)]
    multiplied = 1
    for number in numbers:
        multiplied *= number
        if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
            print('found')
            break
    else:
        print('not found')