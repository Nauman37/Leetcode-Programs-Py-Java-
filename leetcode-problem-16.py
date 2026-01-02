#algorithm to find the lowest value element in an array
my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print('Lowest value:', minVal)
