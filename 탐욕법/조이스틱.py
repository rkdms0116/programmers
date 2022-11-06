def solution(name):
    answer1 = 0
    for n in range(len(name)):
        answer1 += min(ord(name[n]) - ord("A"), ord("Z") + 1 - ord(name[n]))

        if name[n+1:] == "A"*(len(name)-n-1):
            break
         
        answer1 += 1
            
    
    answer2 = min(ord(name[0]) - ord("A"), ord("Z") + 1 - ord(name[0]))+1
    for i in range(len(name)-1,0,-1):
        answer2 += min(ord(name[i]) - ord("A"), ord("Z") + 1 - ord(name[i]))

        if name[1:i] == "A"*(i-1):
            break
            
        answer2 += 1
    print(answer1, answer2)
    return min(answer1,answer2)

solution("JEROEN")
solution("JAN")