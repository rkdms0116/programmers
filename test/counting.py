# k : mylist에 담겨있는 최대의 자연수 값
# 중복된 숫자가 있는 배열에서, 중복된 회수를 카운팅하며 정렬
def CountingSort(mylist, k):
    result = [0] * len(mylist)
    counting = [0] * (k+1)

    for my in mylist:
        counting[my] += 1
    
    for c in range(0, len(counting)-1):
        counting[c+1] += counting[c]
    
    for i in range(len(result)-1, -1, -1):
        result[counting[mylist[i]]-1] = mylist[i]
        counting[mylist[i]] -= 1

    return result
print(CountingSort([0,4,1,3,1,2,4,1], 4))