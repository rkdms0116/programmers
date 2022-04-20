from itertools import permutations
import copy

def solution(expression):
    answer = 0
    operations = ['+', '-', '*']
    opera = []
    number = []
    num = ''
    for ex in expression:
        if ex not in operations:
            num += ex
        else:
            number.append(int(num))
            num = ''
            opera.append(ex)
    else:
         number.append(int(num))

    per_oper = list(permutations(list(set(opera)), len(set(opera))))

    for per in per_oper:
        oper = copy.deepcopy(opera)
        numbers = copy.deepcopy(number)
        # per : 연산의 우선순위 ('+', '-', '*')
        for p in per:
            # 우선순위인 연산자 '+' > '-' > '*'
            while p in oper:
                for i in range(len(oper)):
                    if p == oper[i]:
                        if p == '+':
                            num = numbers[i] + numbers[i+1] 
                        elif p == '-':
                            num = numbers[i] - numbers[i+1] 
                        else:
                            num = numbers[i] * numbers[i+1] 
                        numbers.pop(i+1)
                        numbers.pop(i)
                        numbers.insert(i, num)
                        oper.pop(i)
                        break
                else:
                    break 
        
        if answer < abs(numbers[0]):
            answer = abs(numbers[0])
        
    return answer