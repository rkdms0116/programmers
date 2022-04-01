def solution(number, k):
    answer = ''
    stack = []
    n= 0
    while n < len(number):
        # 남은 k 값이 없다면 남은 값까지 넣어줍니다.
        if k == 0:
            stack.append(number[n:])
            break
        # stack에 들어있다면,
        if stack:
            # 맨 마지막 값과 비교해서 넣어줄 값이 더 크다면
            if stack[-1] < int(number[n]):
                # stack의 마지막 값을 빼줍니다.
                stack.pop(-1)
                k -=1
            # 같거나 크다면 append
            else:
                stack.append(int(number[n]))
                n += 1
        # stack이 비어있어도 append
        else:
            stack.append(int(number[n]))   
            n += 1
    print(stack)
    print(','.join(stack))
    print(stack)
    # list 합치기 
    for s in stack:
        answer += str(s)
    # 만일 k의 값이 남아있다면, 뒤에부터 slicing
    if k:
        answer = answer[:-k]
        
    return answer
print(solution("4177252841",4))