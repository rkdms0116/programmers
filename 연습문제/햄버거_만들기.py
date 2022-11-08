def solution(ingredient):
    answer = 0
    # 만약 재료가 4개 미만이면 햄버거가 만들어질 수 없으므로 return
    if len(ingredient) < 4:
        return answer
    # 3개까지 넣어놓고
    shelf = ingredient[:3]
    for i in range(3, len(ingredient)):
        shelf.append(ingredient[i])
        # 뒤에서부터 4개를 slice 해서 거꾸로 읽었으니, 1,3,2,1의 순서라면 햄버거가 만들어질 수 있으므로 4개를 pop
        if shelf[-1:-5:-1] == [1,3,2,1]:        
            shelf.pop()
            shelf.pop()
            shelf.pop()
            shelf.pop()
            # 포장하는 햄버거 +1
            answer += 1
    return answer