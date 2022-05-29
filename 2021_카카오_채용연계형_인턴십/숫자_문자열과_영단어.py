def solution(s):
    # 숫자와 영단어 대응표
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 
    'six', 'seven', 'eight', 'nine']

    answer = ''
    i=0
    while i < len(s):
        # s[i]가 숫자라면 answer에 바로 대응
        if s[i].isnumeric():
            answer += s[i]
            i += 1
        # 영어로 시작한다면,
        else:
            # 3글자 단위로 글자를 자름(중복되는 영단어가 X)
            find_eng = s[i:i+3]
            for e in range(10):
                if find_eng in eng[e]:
                    answer += str(e)
                    i += len(eng[e])
    return int(answer)

print(solution("one4seveneight"))
print(solution("2three45sixseven"))
