def solution(clothes):
    answer = 1
    spy = {}
    for num in range(len(clothes)):
        name, kind = map(str, clothes[num])
        if kind not in spy:
            spy[kind] = 1
        else:
            spy[kind] += 1
    for val in spy.values():
        answer *= (val + 1)
    return answer-1