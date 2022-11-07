def solution(babbling):
    answer = 0
    # 중복해서 말할 수 없는 단어
    ban = ["ayaaya", "yeye", "woowoo", "mama"]
    # 말할 수 있는 발음
    talk = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling:
        # 먼저 중복해서 말할 수 없는 단어를 ?로 대치
        for b in ban:
            bab = bab.replace(b, "?")
        # 그 후 발음할 수 있는 단어들을 공백으로 대치
        for t in talk:
            bab = bab.replace(t, "0")
    
        # 만일 ?가 존재한다면, 머쓱이가 발음할 수 없으므로 pass
        if "?" in bab:
            pass
        # 빈 문자열이라면(알파벳이 남아있지 않음) > answer += 1
        elif bab.isdigit():
            answer += 1

    return answer