fileObject = open("Data\\text.txt","r")
'''
dataa = fileObject.readline()
print(dataa)
dat = fileObject.readline()
print(dat)
'''
da = fileObject.readlines()
print(da)

'''
for each in da:
    print(each)
   
   
for each in da:
    name,age = each.split(",")
    print("Name: {} and age: {}".format(name,age))
  '''
for each in da:
      name,age = each.split(",")
      age = age[:-1]
      print("Name: {} and Age: {}".format(name,age))  
    