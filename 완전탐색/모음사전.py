from itertools import product

def solution(word):
    dictionary = []
    for i in range(1,6):
        dictionary += list(map(''.join, product("AEIOU", repeat=i)))
    dictionary.sort()

    cnt = dictionary.index(word)
    print(cnt)
    return ''

solution("AAAE")