# 나의 코드
a, b = map(int, input().strip().split(' '))
print(a//b, a%b)


# 앞으로 가야할 코드 방향
# !!divmod는 큰 수에서 더 효율적!!
a, b = map(int, input().strip().split(' '))
print(*divmod(a, b))