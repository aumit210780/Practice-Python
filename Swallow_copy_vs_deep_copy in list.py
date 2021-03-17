import copy
print(copy)
lis1 = [1,2,3,4,5,[1,2],7]
lis2 = lis1[:]
print(lis1)
print(lis2)
lis2[5].append(3)
print(lis1)
print(lis2)
#That means in nested list, swallow copy doesn't works
lis3 = [1,2,3,[1,2,True],5]
lis4 = copy.copy(lis3)
print(lis3)
print(lis4)
lis4[3].append(3)
print(lis4)
print(lis3)
#This only copy also doesn't work
#So original method is:
lis5 = [1,2,3,4,[1,3,4,"Raju"],"Anik"]
lis6 = copy.deepcopy(lis5)
lis6[4].append("Adib")
print(lis5)
print(lis6)

