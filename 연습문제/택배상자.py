def solution(order):
    # 보조 컨테이너
    sub_con = []
    # 메인 컨테이너
    main_con = []
    # order의 순서를 확인할 index
    idx = 0
    # 컨테이너 벨트에서 나오는 상자 번호
    n = 1
    
    while idx < len(order):
        # 만일 컨테이너 벨트에서 나온 상자가 주문과 일치한다면
        if order[idx] == n :
            main_con.append(n)
            idx += 1
            n += 1
        # 보조 컨테이너의 마지막 상자가 주문 순서와 같을 경우
        elif sub_con and sub_con[-1] == order[idx]:
            main_con.append(sub_con.pop())
            idx += 1
        else:
            # 컨테이너 벨트는 n까지만 나올 수 있으므로 check
            if n == len(order)+1:
                return len(main_con)
            # 어디에도 해당되지 않은 상자는 보조 컨테이너 벨트에 담아줍니다.
            sub_con.append(n)
            n += 1
    return len(main_con)
