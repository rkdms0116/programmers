import math

def solution(arrayA, arrayB):
    # arrayA의 최대공약수 구하기
    if len(arrayA) == 1:
        gcdA = arrayA[0]
    else:
        gcdA = find_gcd(arrayA)
    
    # arrayB의 최대공약수 구하기
    if len(arrayB) == 1:
        gcdB = arrayB[0]
    else:
        gcdB = find_gcd(arrayB)
    
    # 두 배열의 최대 공약수 list를 내림차순으로 정렬하기 
    find_li = sorted([gcdA, gcdB], reverse=True)

    # 최대공약수의 값이 어떤 배열의 최대공약수인지 확인 후 > 해당 배열의 최대공약수는 모든 숫자를 나눌 수 있음
    # 나눌 수 없는 배열을 확인하여 array로 지정
    for fi in find_li:
        if gcdA%fi == 0:
            array = arrayB
        elif gcdB%fi == 0:
            array = arrayA
        else:
            break
        # array를 돌아보면서 하나도 나눌 수 없는 정수임을 check   
        for arr in array:
            if arr%fi == 0:
                break
        else:
             return fi
    else:
        return 0
                    
# 최대공약수를 찾아본다! > 유클리드 호제법
def find_gcd(array):
    gcd = array[0]
    
    for i in range(1, len(array)):
        
        if gcd == 1:
            return gcd
        
        a, b = max(gcd, array[i]), min(gcd, array[i])
        while True:
            q, r = divmod(a, b)
            if r == 0:
                gcd = b
                break
            else:
                a, b = b, r
    return gcd