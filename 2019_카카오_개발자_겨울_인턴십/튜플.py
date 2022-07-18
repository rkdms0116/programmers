def solution(s):
    words = s[2:-2]
    li = words.split('},{')
    answer = []
    li.sort(key=len)
    for l in li:
        num = l.split(',')
        for n in num:
            if int(n) not in answer:
                answer.append(int(n))
    return answer