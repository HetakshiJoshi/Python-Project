tuple1 = (1,2,3,4,8)

#assignment 1 = replace 8 by 5 in given tuple
list1 = list(tuple1)
print(list1)
list1[4]=5
print(list1)

#assignment 2 = extend [6,7,8,9,10] in given tuple
list1.extend([6,7,8,9,10])
print(list1)
tuple2 = tuple(list1)
print(tuple2)