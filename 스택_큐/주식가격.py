from collections import deque

def solution(prices):
    answer = []
    stocks = deque(prices)
    
    while stocks:
        # 가장 왼쪽 주식 값 추출
        stock = stocks.popleft()
        time = 0
        # 남아있는 주식들의 가격을 확인하면서
        for price in stocks:
            time += 1
            # 왼쪽 값이 더 큰 순간 멈춤
            if stock > price:
                break
        # for문이 정상적으로 끝나거나 break 걸려도 값 추가
        answer.append(time)
    return answer
