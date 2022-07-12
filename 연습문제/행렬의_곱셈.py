def solution(arr1, arr2):
    answer = list([0]*len(arr2[0]) for _ in range(len(arr1)))
    for i in range(len(arr1)):
        for k in range(len(arr2[0])):
            val = 0
            for j in range(len(arr1[0])):
                val += arr1[i][j] * arr2[j][k]
            answer[i][k] = val
    return answer