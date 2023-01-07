from collections import deque
def solution(begin, target, words):
    answer = 0
    # 정답을 append
    words.append(begin)
    # 정답이 words에 없을 경우
    if target not in words:
        return 0

    que = deque([target])
    words.remove(target)
    while words:
        temp = deque()
        answer += 1
        # bfs 실시
        for ele in que:
            for word in words:
                # 만일 한 개가 변환할 수 있다면
                if dif_word(ele, word):
                    # 정답이라면
                    if word == begin:
                        return answer
                    words.remove(word)
                    temp.append(word)
        que = temp
    return 0

# 단어의 변환 과정
def dif_word(w1, w2):
    cnt = 0
    for w in range(len(w1)):
        if w1[w] != w2[w]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False
print(solution("aab", "aba", ["abb","aba"]))
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))