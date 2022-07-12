def solution(n):
    answer = 0
    for i in range(1, n//2+2):        
        temp = 0
        for j in range(i, n):
            temp += j
            if temp > n:
                break
            if temp == n:
                answer += 1
                break
    return answer + 1
