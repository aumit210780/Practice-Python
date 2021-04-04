#Find squares of each from 1 to 10 
print("Find squares of each from 1 to 10")
data = []
for i in range(1,11):
    data.append(i**2)
print(data)
print()
print("Alternative Way: ")
data2 = [i**2 for i in range(1,11)]
print(data2)
print()
data3 = [i*3 for i in range(0,11,2)]
print(data3)
print()
