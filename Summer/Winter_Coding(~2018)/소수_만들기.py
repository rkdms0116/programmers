from itertools import combinations
import math

def solution(nums):
    answer = 0
    
    comList = list(combinations(nums, 3))
    
    for comb in comList:
        num = 0
        for c in comb:
            num += c
        
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                break
        else:
            answer += 1
                
    # print(sumList)
    return answer