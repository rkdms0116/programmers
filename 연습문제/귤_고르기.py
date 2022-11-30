def solution(k, tangerine):
    answer = 0
    # 귤 사이즈를 key, 개수를 value로 갖는 dict
    tan_dict = dict()
    for tan in tangerine:
        if tan in tan_dict:
            tan_dict[tan] += 1
        else:
            tan_dict[tan] = 1
            
    # value가 큰 순서대로 정렬
    sorted_tan = sorted(tan_dict.items(), key=lambda i:i[1], reverse=True)

    # k개 고르기
    for s in sorted_tan:
        num = s[1]
        if k < num:
            break
        elif k==0:
            return answer
        k -= num
        answer += 1
        
    # 만일 k가 0으로 남아있지 않는 case, 한 가지의 종류를 +1 해서 return
    if k == 0:
        return answer
    else:
        return answer+1