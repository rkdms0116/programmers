def SelectionSort(mylist):
    for i in range(len(mylist)):
        min_idx = i
        for j in range(i, len(mylist)):
            if mylist[j] < mylist[min_idx]:
                min_idx = j
        mylist[i], mylist[min_idx] = mylist[min_idx], mylist[i]
    return mylist

print(SelectionSort([3,6,8,2,6,9]))