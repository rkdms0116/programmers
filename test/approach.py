mylist = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for x in range(len(mylist[0])):
    for y in range(len(mylist)):
        print(mylist[y][x], end=' ')
