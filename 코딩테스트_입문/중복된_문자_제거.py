def solution(my_string):
    answer=list()
    for my in my_string:
        if my not in answer:
            answer.append(my)
    return ''.join(answer)