def solution(food):
    temp = ''
    for f in range(1, len(food)):
        temp += str(f) * (int(food[f])//2) 
    temp += '0'
    answer = temp
    for t in range(len(temp)-2, -1, -1):
        answer += temp[t]
    return answer

def solution(food):
    answer = ''
    stack = []
    for f in range(1, len(food)):
        stack.append(str(f) * (int(food[f])//2)) 
    first = "".join(stack)
    answer = first + "0" + first[::-1]
    return answer