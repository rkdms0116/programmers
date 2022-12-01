def solution(want, number, discount):
    answer = 0
    # 시작하는 날짜는 s_day로 지정
    for s_day in range(len(discount)-9):
        # want를 key, number를 value로 하는 dict 생성
        basket = {want[i]:number[i] for i in range(len(want))}
        # 열흘동안
        for d_day in range(10):
            # 할인 품목이 basket의 안에 존재하고, 물량이 0 이상이라면,
            if discount[s_day + d_day] in basket and basket[discount[s_day + d_day]] > 0:
                basket[discount[s_day + d_day]] -= 1
            else:
                break
        # 모든 것을 만족할 때에 answer ++
        else:
             answer += 1   
    return answer
