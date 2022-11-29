def solution(cards):
    answer = 0
    box_list = [0]
    idx=0
    temp = set()
    # cards가 0인 list가 될 때까지
    while cards != [0] *len(cards):
        # temp에 card가 없고, 0이 아닌 경우
        if cards[idx] not in temp and cards[idx] != 0:
            temp.add(cards[idx])
            ## 코드 좀 예쁘게 하고 싶은 부분...!
            n_idx = cards[idx]-1
            cards[idx] = 0
            idx = n_idx
            
        else:
            # 길이만 확인할 것이라서 len으로
            box_list.append(len(temp))
            temp = set()
            for c in range(len(cards)):
                if cards[c] != 0:
                    idx = c
                    break
    box_list.append(len(temp))
    # 만약 상자가 한 개 라면 return 0
    # # 아니면 box_list에 0을 넣어두고 계산
    # if len(box_list)==1:
    #     return 0
    # else:
    box_list.sort(reverse=True)
    return box_list[0]*box_list[1]
