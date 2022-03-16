n, clockwise = map(str, input().split())
n = int(n)
result = list([0]*int(n) for _ in range(int(n)))

# True일 때, 
TdirX = [1, 0, -1, 0]
TdirY = [0, 1, 0, -1]
TresultX = [-1, n-1, n, 0]
TresultY = [0, -1, n-1, n]

# False일 때, 하우상좌
FdirX = [0, 1, 0, -1]
FdirY = [1, 0, -1, 0]
FresultX = [0, -1, n-1, n]
FresultY = [-1, n-1, n, 0]

if clockwise == "True":
    vecX = TdirX
    vecY = TdirY
    cX = TresultX
    cY = TresultY
else:
    vecX = FdirX
    vecY = FdirY
    cX = FresultX
    cY = FresultY

num = n**2//4
i = 0
c = 0

while i < num:
    i += 1
    for ea in range(4):
        nx = cX[ea] + vecX[(c+ea)%4]
        ny = cY[ea] + vecY[(c+ea)%4]

        if -1<nx<n and -1<ny<n and not(result[ny][nx]):
            result[ny][nx] = i
            cX[ea] += vecX[(c+ea)%4]
            cY[ea] += vecY[(c+ea)%4]  
        else:
            nx = cX[ea] - vecX[(c+ea)%4]
            ny = cY[ea] - vecY[(c+ea)%4]
            c += 1
            i -= 1
            break

# n이 홀수이면 중앙에 한 개의 값
if n%2:
    result[n//2][n//2] = num+1

print(result) 