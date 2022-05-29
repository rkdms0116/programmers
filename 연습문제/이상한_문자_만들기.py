def solution(s):
    answer = ''
    word_list = list(s.split(" "))
    for word in word_list:
        for w in range(len(word)):
            if w%2:
                answer += word[w].lower()
            else:
                answer += word[w].upper()
        answer += " "
    return answer[:-1]
li = [2,1,5,3]
print(remove(li[0]))