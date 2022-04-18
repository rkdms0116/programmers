from itertools import combinations 
def solution(numbers, target):
    # numbers의 인덱스로 list 만들기
    num_idx = [i for i in range(len(numbers))]
    # numbers의 인덱스로 조합
    result = []
    for i in range(len(numbers)+1):
        result = result+list(combinations(num_idx,i))  
    # target과 일치하는 개수
    cnt = 0
    
    # 조합 하나하나를 순회하면서
    for plus_set in result:
        makenum = 0
        for i in range(len(numbers)):
            # index가 순회한 조합에 있으면 +
            if i in plus_set:
                makenum += numbers[i]
            # index가 순회한 조합에 없으면 -    
            else:
                makenum -= numbers[i]
        # 만들어진 숫자가 타겟과 일치할 때 cnt ++
        if makenum == target:
            cnt += 1
            
    return cnt