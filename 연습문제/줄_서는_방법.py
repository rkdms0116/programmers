import math

def solution(n, k):
    answer = []
    numList = [i for i in range(1, n+1)]
    while n != 0:
        temp = math.factorial(n-1) 
        idx = k // temp
        k = k % temp
        if k == 0:
            answer.append(numList.pop(idx-1))
        else :
             answer.append(numList.pop(idx))

        n -= 1
    
    return answer