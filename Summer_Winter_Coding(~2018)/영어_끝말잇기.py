from tkinter import W


def solution(n, words):
    game = []
    answer = []
    idx = 0
    while idx < len(words):
        word = words[idx]
        if word not in game:
            if idx == 0 or (idx != 0 and game[-1][-1] == word[0]):
                game += [word]
            else:
                break


    return answer