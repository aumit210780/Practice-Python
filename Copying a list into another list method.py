lis1 = [1,2,3,4,5,6]
lis2 = lis1
print(lis1)
print(lis2)
lis2.append(7)
print(lis2)
print(lis1)
#That means copying a list using list1 = list2 will copy the address. So any changes in one list will also affect the other.
lis3 = [1,2,3,4,5,6,7,8,9]
lis4 = lis3[:]
print(lis3)
print(lis4)
lis4.append(10)
print(lis4)
print(lis3)
#This is one method of copying one list from another
#Another Method is:
lis5 = [9,8,7,6,5,4,3,2]
lis6 = list(lis5)
print(lis5)
print(lis6)
lis6.append(1)
print(lis6)
print(lis5)