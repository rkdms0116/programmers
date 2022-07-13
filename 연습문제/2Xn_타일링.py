def solution(n):
    answer = [0] * 60001
    answer[1], answer[2] = 1, 2
    i = 3
    while i != n+1:
        answer[i] = (answer[i-1] + answer[i-2])%1000000007
        i += 1
    return answer[n]