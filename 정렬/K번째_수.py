def solution(array, commands):
    answer = []
    # commands = [i, j, k] : i번째부터 j번째까지 슬라이스 하여 정렬하였을 때 k번째의 수
    for c in commands:
        slice_array = array[c[0]-1:c[1]]
        sort_array = sorted(slice_array)
        answer += [sort_array[c[2]-1]]
        # answer.append(sort_array[c[2]-1])
    return answer