'''
fileobject = open("Data\\text.txt","w")
fileobject.write("Heyyy I am new")
fileobject.close()
'''
# Here 'w' write function overwrite the before data of that file
#So we use append function to add new data on the existing file
fileobject = open("Data\\text.txt","a")
fileobject.write("\nHey I am new data, I am here because of append function")
fileobject.close()