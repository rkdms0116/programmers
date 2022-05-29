def solution(s):
    answer = 0
    for i in s:
        if i == "p" or i == "P":
            answer += 1
        elif i == "y" or i == "Y":
            answer -= 1
    # p와 y의 개수가 같으면 True, 아니면 False
    if answer == 0:
        return True
    else:
        return False