from math import sqrt

def solution(left, right):
    answer = 0
    
    for num in range(left, right+1):
        # 약수의 개수가 홀수 === 제곱근이 정수
        if sqrt(num) == int(sqrt(num)):
            answer -= num
        else:
            answer += num
    return answer

print(solution(13,17))
print(solution(24,27))