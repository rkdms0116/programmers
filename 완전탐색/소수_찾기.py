import math
from itertools import permutations

def solution(numbers):
    answer = 0
    # 순열로 만든 숫자들을 집합으로 만들어 둘 집합(중복 제거)
    make_num = set()
    # numbers의 숫자를 찢어 넣어둠
    num_sep = []
    for num in numbers:
        num_sep.append(num)

    for sep in range(1, len(num_sep)+1):
        # 1개 이상의 순열들을 list로 담아서 num_per에 넣음
        num_per = list(permutations(num_sep, sep))
        # num_per에 들어간 순열을 join하여 int로 변환 후('017' == '17') make_num 집합에 넣음
        for per in num_per:
            num = int(''.join(per))
            make_num.add(num)
    # 소수 찾기
    for n in make_num:
        if n > 1:
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    break
            else:
                answer += 1
    return answer
