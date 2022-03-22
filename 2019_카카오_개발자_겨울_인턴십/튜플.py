def solution(s):
    answer = ""
    s = s[1:-1]
    temp1 = s.replace('{', '[')
    temp2 = temp1.replace('}', ']')
    
    i = 0
    temp = ""
    while i < len(temp2):

        if temp2[i] == "]":
            temp += temp2[i]
            if len(temp) > len(answer):
                answer = temp
            temp = ""
            i += 1

        if i >= len(temp2):
            break
        temp += temp2[i]
        i += 1
                    
    return answer

s = "{{20,111},{111}}"
print(solution(s))