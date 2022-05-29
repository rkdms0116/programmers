def solution(arr, divisor):
    answer = []
    for a in arr:
        if not(a%divisor):
            answer.append(a)
    # answer가 존재하면 오름차순 정렬
    if answer:
        answer.sort()
    # answer가 존재하지 않으면 -1 append
    else:
        answer = [-1]
    return answer