def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    
    while bridge:
        # 다리를 건너는 트럭
        bridge.pop(0)
        # 대기중인 트럭의 list가 남아있는가
        if truck_weights:
            # 다리 위에 있는 트럭들의 무게가 견딜 수 있는가
            if truck_weights[0] + sum(bridge) > weight:
                bridge.append(0)
            else:
                bridge.append(truck_weights.pop(0))
        answer += 1
    return answer