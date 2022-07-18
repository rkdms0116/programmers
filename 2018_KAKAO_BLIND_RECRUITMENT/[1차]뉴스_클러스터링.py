from collections import Counter

def solution(str1, str2):
    # 문자열 대문자로 만들기
    str1 = str1.upper()
    str2 = str2.upper()
    # 2글자 잘라서 담을 list
    str1_list = []
    str2_list = []
    # str1과 str2를 돌면서 각각의 단어가 영문자로 이루어진 쌍일 때 list에 담기
    for s1 in range(len(str1)-1):
        if str1[s1].isalpha() and str1[s1+1].isalpha():
            str1_list.append(str1[s1:s1+2])
    for s2 in range(len(str2)-1):
        if str2[s2].isalpha() and str2[s2+1].isalpha():
            str2_list.append(str2[s2:s2+2])
    # 만일 A와 B가 모두 공집합일 경우 1 * 65536 값 return
    if not(str1_list) and not(str2_list):
        return 65536
    
    # 교집합의 개수 세어줌
    inter_cnt = 0
    for l in str1_list:
        if l in str2_list:
            inter_cnt += 1
            str2_list.remove(l)
    return int(inter_cnt/(len(str1_list) + len(str2_list))*65536)