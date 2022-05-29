def solution(strings, n):
    answer = []
    # 1. string의 n번째 알파벳(value)과 인덱스(key)를 저장하는 dictionary 만들기
    my_dict = dict()
    for s in range(len(strings)):
        my_dict[s] = strings[s][n:n+1]

    # 2. dictionary의 value에따라 오름차순 정렬
    sort_dict = sorted(my_dict.items(), key = lambda i : i[1])
    # 3. 정렬된 오름차순의 인덱스(key)에 해당되는 string을 list에 담기
    for s in sort_dict:
        answer.append(strings[s[0]])
    return answer

solution(["sun", "bed", "car"], 1)