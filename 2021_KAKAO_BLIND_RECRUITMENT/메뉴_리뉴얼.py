from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        combi_dic = {}
        for order in orders:
            # orders에 있는 것들 중에서 c개의 조합을 찾아봅니다.
            combi = combinations(order, c)
            # 조합들 속에서
            for com in combi:
                # com의 조합으로 temp에 저장
                temp = ''.join(sorted(com))
                # combi_dic에 dictionary형태로 저장(개수까지 세어주면서)
                if temp in combi_dic:
                    combi_dic[temp] += 1
                else:
                    combi_dic[temp] = 1
        # value의 값을 기준으로 내림차순 정렬
        sorted_combi = sorted(combi_dic.items(), key = lambda item: item[1], reverse = True)

        # sorted_combi가 존재하면서, 2팀 이상이 주문을 했을 때 계산
        if sorted_combi and sorted_combi[0][1] > 1:
            # 최댓값 저장
            menu_max = sorted_combi[0][1]
            for menu in sorted_combi:
                if menu[1] == menu_max:
                    answer.append(menu[0])
                else:
                    break
    return sorted(answer)

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))