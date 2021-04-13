from os.path import exists
file_name = input("Enter file name: ")
if exists(file_name):
    with open(file_name,"r") as fileobject:
        print(fileobject.read())
else:
    print("File not found")