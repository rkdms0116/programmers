from collections import deque
def solution(cacheSize, cities):
    answer = 0
    # cacheSize가 0일 경우 
    if cacheSize == 0:
        return 5*len(cities)
    
    buffer = deque()
    # buffer의 size를 확인하는 flag
    buffer_flag = False
    
    for city in cities:
        # cache는 대소문자 구분하지 않으므로
        city = city.lower()
        # buffer에 city가 있을 경우, 제거해주고 answer +1
        if city in buffer:
            buffer.remove(city)
            answer += 1
        # buffer에 없을 경우, answer +5
        else:
            answer += 5
            # buffer의 size가 cacheSize까지 넘었었을 경우, 계속 넘을 경우만 생기므로
            if buffer_flag:
                # 가장 오래된 cache를 지움
                buffer.popleft()
            else:
                # 추후에 append해줄 것이므로 현재 bufferSize에 +1을 했을 때, cacheSize가 된다면 flag True로 변환
                if len(buffer) + 1 == cacheSize:
                    buffer_flag = True
        # buffer에 city 추가
        buffer.append(city)
    return answer