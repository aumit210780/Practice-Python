fileObject = open("Data\\text.txt","r")
'''
dataa = fileObject.readline()
print(dataa)
dat = fileObject.readline()
print(dat)
'''
da = fileObject.readlines()
print(da)
finalda = []

'''
for each in da:
    print(each)
   
   
for each in da:
    name,age = each.split(",")
    print("Name: {} and age: {}".format(name,age))
  '''
for each in da:
      name,age = each.split(",")
      finalda.append((name,age))
      if "\n" in age:
          age = age[:-1]
          print("Name: {} and Age: {}".format(name,age))
      else:
          print("Name: {} and Age: {}".format(name,age))
print(finalda)
print() 
finalda.sort(key=lambda a:a[1]) 
print(finalda)
          