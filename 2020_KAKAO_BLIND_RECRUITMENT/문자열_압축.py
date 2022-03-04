def solution(s):
    answer = len(s)
    # 자르는 길이 절반까지 확인
    for cut in range(1, len(s)//2+1):
        # 반복하는 횟수
        cnt = 1
        compare_word = s[:cut]
        cut_word = ""
        
        for i in range(cut, len(s)+cut, cut):
            # 반복되는 값일 때 cnt ++
            if compare_word == s[i:i+cut]:
                cnt += 1
            # 반복되는 값이 아닐 때 
            else:
                if cnt == 1:
                    cut_word += compare_word
                else:
                    cut_word += str(cnt) + compare_word
                compare_word = s[i:i+cut]
                cnt =1
        # 정답에 더 짧은 값으로 할당
        answer = min(answer, len(cut_word))
    return answer