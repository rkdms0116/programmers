def solution(n, words):
    used = []
    for w in range(len(words)):
        # 단어의 사용 여부 확인
        if words[w] in used:
            return [w%n+1, w//n+1]
        else:
            # used에 단어가 있을 경우
            if used:
                # 마지막 사용된 단어의 마지막 알파벳과, 들어갈 단어의 첫 알파벳 확인
                if used[-1][-1] == words[w][0]:
                    used.append(words[w])
                else:
                    return [w%n+1, w//n+1]
            # used가 빈 list일 경우 단어를 넣어줌
            else:
                used.append(words[w])
    # 탈락자가 생기지 않을 시
    return [0, 0]
