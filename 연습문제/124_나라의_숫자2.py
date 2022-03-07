def solution(n):
    answer = ''
    # 새로운 n진법 만들기
    n_world = ['1', '2', '4']
    while n:
        # n_world의 index와 3으로 나누었을때의 나머지를 맞춤
        n -= 1
        answer += n_world[n%3]
        n = n//3
    return answer[::-1]