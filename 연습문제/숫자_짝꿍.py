def solution(X, Y):
    answer = ''
    # X와 Y에 나오는 숫자들을 최소한으로 count해준다.
    num_set = sorted(set(X) & set(Y), reverse=True)
    # num_set 안에 있는 값들을 확인하며 answer에 대입해준다.
    for n in num_set:
        answer += str(n) * min(X.count(str(n)), Y.count(str(n)))

    # answer가 존재하면
    if answer:
    	# 처음이 0이면 무조건 0으로 return
        if answer[0] == '0':
            return "0"
        else:
            return answer
    else:
        return "-1"