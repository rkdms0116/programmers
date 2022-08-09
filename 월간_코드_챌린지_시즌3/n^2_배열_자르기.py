def solution(n, left, right):
    arr = []
    for i in range(left, right+1):
        # 몫과 나머지 중 큰 값 +1을 return할 배열에 넣어줌
        q = i//n
        r = i%n
        arr.append(max(q,r)+1)
    return arr


'''
시간초과
def solution(n, left, right):
    # 2차원 배열을 생성해준다!
    arr2 = [[0]*n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            arr2[j][i] = max(i,j) + 1
    # 1차원 배열로 바꿔준다!
    arr1 = []
    for a in arr2:
        arr1+= a
    # left에서 ringt index까지 return
    return arr1[left:right+1]
    '''