def solution(numbers, hand):
    answer = ''
    now_L = 10
    now_R = 12
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            now_L = number
        elif number in [3,6,9]:
            answer += 'R'
            now_R = number
        else:
            if number == 0:
                number = 10
            dis_L = abs(now_L - number)
            dis_R = abs(now_R - number)
            if dis_L < dis_R:
                answer += 'L'
                now_L = number
            elif dis_R < dis_L:
                answer += 'R'
                now_R = number
            else:
                if hand == 'right':
                    answer += "R"
                    now_R = number
                else:
                    answer += "L"
                    now_L = number
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))