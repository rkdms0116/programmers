def solution(ingredient):
    answer = 0
    total = "".join(map(str, ingredient))
    while "1231" in total:
        total = total.replace("1231", "", 1)
        answer += 1
    return answer

solution([2, 1, 1, 2, 3, 1, 2, 3, 1])