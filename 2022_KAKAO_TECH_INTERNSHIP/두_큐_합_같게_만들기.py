from collections import deque

def solution(queue1, queue2):
    que1 = deque(queue1)
    que2 = deque(queue2)
    sum1 = sum(que1)
    sum2 = sum(que2)
    # # queue1과 queue2의 합이 홀수면 두 개의 큐의 각각의 합을 같게 만들 수 없으므로 -1 return
    # # 근데 없어도 코드 잘 돌아감..
    # if (sum1 + sum2) % 2:
    #     return -1
    
    for cnt in range(len(que1)+ len(que2)+5):
        # que1의 합과 que2의 합이 같으면 실행 횟수 return
        if sum1 == sum2:
            return cnt
        # queue1의 합이 더 크면 queue1에서 pop해서 queue2에 append
        elif sum1 > sum2:
            el = que1.popleft()
            que2.append(el)
            sum2 += el
            sum1 -= el
        else:
            el = que2.popleft()
            que1.append(el)
            sum1 += el
            sum2 -= el
    # 횟수만큼 실행해도 return이 안되었다면 -1 return
    else:
         return -1   