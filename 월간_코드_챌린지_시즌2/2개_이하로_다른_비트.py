def solution(numbers):
    answer = []
    # numbers에 있는 num들을 하나씩 돌면서
    for num in numbers:
        # 0bxxxx로 되어있을 때, 오른쪽에서부터 0을 찾습니다
        bit_1 = bin(num)[2:].rfind('0')
        # 비트에서 0이 없다면
        if bit_1 == -1:
            next_num = bin(num)[:2] + '10' + '1' * (len(bin(num))-3)
            answer.append(int(next_num,2))
        # 비트에 0이 있다면, 0이 나타난 순간부터 10으로 바꿔주거나, 0을 1로 바꿔줍니다.
        else:
            next_num1 = bin(num)[:2+bit_1] + '10' + bin(num)[bit_1+4:]
            next_num2 = bin(num)[:2+bit_1] + '1' + bin(num)[bit_1+3:]
            answer.append(min(int(next_num1,2), int(next_num2,2)) )
    return answer

'''
오답 및 시간초과
def solution(numbers):
    answer = []
    # numbers에 있는 num들을 하나씩 돌면서
    for num in numbers:
        # num 값보다 큰 값들을 하나씩 비교해가면서
        for n in range(num+1, num*10**2):
            xor_bin = bin(num^n)
            # 만일 1의 개수가 1개 혹은 2개이면 answer에 추가
            if xor_bin.count('1') == 1 or xor_bin.count('1') == 2:
                answer.append(n)
                break
    return answer
'''