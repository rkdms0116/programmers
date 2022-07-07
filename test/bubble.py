def BubbleSort(mylist):
    for a in range(len(mylist)-1, 0, -1):
        for b in range(0, a):
            if mylist[b] > mylist[b+1]:
                mylist[b], mylist[b+1] = mylist[b+1], mylist[b]
    return mylist

print(BubbleSort([10, 6, 7, 3, 8, 1]))