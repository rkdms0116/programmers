# 소수 찾는 함수
def isPrime(num):
    if num > 1:  
        for i in range(2,int(num**(1/2)+1)):  
            if (num % i) == 0:  
                return False
        return True
    else:
        return False

# 10진수인 num을 k진수로 변환시켜주는 함수
def numChange(num, k):
    rev_base = ''

    while num > 0:
        num, mod = divmod(num, k)
        rev_base += str(mod)

    return rev_base[::-1]
    
def solution(n, k):
    answer = 0
    # k진법으로 변환
    knum = numChange(n, k)
    # 0을 기준으로 쪼개어줌(중복을 허락하므로 list로)
    klist = list(knum.split('0'))
    for k in klist:
        # 숫자이면서, 소수이면 answer ++
        if k.isdigit() and isPrime(int(k)):
            answer += 1
    return answer