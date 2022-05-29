def solution(check_words):
    if check_words:
        open_cnt = 0
        for i in range(1, len(check_words)):
            word = check_words[:i]
            if word.count("(") == word.count(")"):
                u = word
                v = check_words[i:]
                print(u, v)
                break
    # 빈 문자열일 경우
    else:
        return ""

solution("()))((()")

def check(check_words):
    cnt = 0
    for word in check_words:
        if cnt < 0 :
            change(check_words)

        if word == "(":
            cnt += 1
        else:
            cnt -=1

def change(check_words):
    pass