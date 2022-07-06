# 나의 코드
s, n = input().strip().split(' ')
n = int(n)
print(s+' '*(n-len(s)))
print(' '*((n-len(s))//2) + s + ' '*((n-len(s))//2))
print(' '*(n-len(s))+s)


# 앞으로 가야할 코드 방향
s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬