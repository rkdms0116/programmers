def solution(lottos, win_nums):
    zero_cnt = 0
    win_cnt = 0
    answer = [0, 0]
    for num in range(6):
        if lottos[num] == 0:
            zero_cnt += 1
        elif lottos[num] in win_nums:
            win_cnt += 1
    zero_cnt += win_cnt

    if win_cnt > 0:
        answer[1] = 7- win_cnt
    else:
        answer[1] = 6
    if zero_cnt > 0:
        answer[0] = 7- zero_cnt
    else:
        answer[0] = 6

    return answer