#bubble sort program
mylist = [7, 3, 9, 12, 11, 1,0, 5, 101, 4, 6, 101.1, -3]#this is a sample list,you can your own list here

n = len(mylist)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if mylist[j] > mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
            swapped = True
    if not swapped:
        break
print(mylist)