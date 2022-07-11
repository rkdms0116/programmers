# 두개씩 뽑아서 최소공배수를 찾아나섬
def solution(arr):
    # 최소공배수
    n1 = arr.pop(0)
    while arr:
        n2 = arr. pop(0)
        # 최대공약수 gcd
        gcd = 1
        for n in range(2, min(n1, n2)+1):
            if not(n1%n) and not(n2%n):
                gcd = n
        n1 = int(n1/gcd) * int(n2/gcd) * gcd
    return n1

solution([1,2,3])

"""
from fractions import gcd

def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2,6,8,14]));
"""