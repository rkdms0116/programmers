def solution(phone_book):
    for num1 in range(len(phone_book)):
        for num2 in range(num1+1, len(phone_book)):
            if phone_book[num1] in phone_book[num2]:
                return False
    else:
        return True

solution(["123","456","789"])