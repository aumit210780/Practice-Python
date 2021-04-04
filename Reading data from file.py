'''
w->for write
r->for read
a->for append
'''
fileObject = open("Data\\text.txt","r")
dataa = fileObject.read()
print(dataa)
print(len(dataa))
