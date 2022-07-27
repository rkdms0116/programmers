import math

def solution(begin, end):
    answer = []
    for step in range(begin, end+1):
        if step < 2:
            answer.append(0)
        elif step < 4:
            answer.append(1)
        else:
            for n in range(2, int(math.sqrt(step))+1):
                if step//n>10000000:
                    continue
                if not(step%n):
                    answer.append(step//n)
                    break
            else:
                 answer.append(1)
    return answer
