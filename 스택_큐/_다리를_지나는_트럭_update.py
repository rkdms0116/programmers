from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = deque([0] * bridge_length)
    waiting_truck = deque(truck_weights)
    bridge_weight = 0

    while waiting_truck:
        bridge_weight -= bridge.popleft()
        if waiting_truck:
            if bridge_weight + waiting_truck[0] > weight:
                bridge.append(0)
            else:
                now_truck = waiting_truck.popleft()
                bridge.append(now_truck)
                bridge_weight += now_truck

        answer += 1
    return answer
"""변형해서 아직..."""