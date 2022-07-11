'''
def solution(s):
    words = list(s.split())
    answer = ''
    for word in words:
        answer += word[0].upper() + word[1:].lower()+ ' '
    return answer
'''
    

def solution(s):
    answer = ''
    words = s.split(' ')

    for word in words:
        if word == '':
            answer += ' '
        else:
            answer += word[0].upper() + word[1:].lower() + ' '

    return answer[:-1]

def Jaden_Case(s):
    # 함수를 완성하세요
    return s.title()