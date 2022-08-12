from itertools import permutations

def solution(k, dungeons):
    answer = -1
    # 던전 순서를 순열로 만들어줌
    per_dungeon = list(map(list,permutations(dungeons)))
    # 던전 순서
    for dungeon in per_dungeon:
        # 탐험할 수 있는 던전의 개수 
        cnt = 0
        # k의 값 새로 갱신
        stamina = k
        # 던전 순서 당 하나씩 돌면서
        for dun in dungeon:
            # 만일 최소 필요 피로도보다 작으면, 끝
            if dun[0] > stamina:
                break
            # 던전을 돌 수 있는 피로도라면, 소모 필요도만큼 피로도에서 차감
            else:
                stamina -= dun[1]
                cnt += 1 
                # 최대 던전을 돌 수 있는 개수 확인
                if cnt > answer:
                    answer = cnt
    return answer