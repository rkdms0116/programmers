def solution(seoul):
    for s in range(len(seoul)):
        if seoul[s] == "Kim":
            # return 혹은 print 문에 변수를 선언하는 방법(d: 십진수, f: 실수, s: 문자열)
            return "김서방은 %d에 있다"%s

print(solution(["Jane", "Kim"]))
