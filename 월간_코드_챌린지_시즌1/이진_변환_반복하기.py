def solution(s):
    # answer[실행횟수, 제거된 0의 개수]
    answer = [0, 0]
    while True:
        # 만약 s가 1이면 break
        if s == '1':
            return answer
        # s의 0의 개수
        zero = s.count('0')
        # 남은 길이의 이진법으로 변환
        s = bin(len(s) - zero)[2:]
        answer[0] += 1
        answer[1] += zero