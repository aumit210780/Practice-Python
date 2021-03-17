lis1 = [11,7,5,15,-9]
print(lis1)
lis1.sort()  #It manipulate the original data and sort it into ascending order
print(lis1)
lis1.sort(reverse=True) #It manipulate the original data and sort it into descending order

print(lis1)
lis1.sort(reverse=False) #It manipulate the original data and sort it into ascending order
print(lis1)

#Now if you don't want to manipulate original list but want to sort then follow this in below:
lis2 = [11,5,6,45,55,98,90]
lis3 = sorted(lis2)
print(lis2)
print(lis3)