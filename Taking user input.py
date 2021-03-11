name = input("Enter your name: ")
print(name)
age = input("Enter your Age: ") #Input is always by default string
print(type(age))

print(name,age,sep="\n") #Here \n gives new line
print("You have to typecast for getting right data type...",sep="\n")

name1 = input("Enter your friend name here: ")
age1 = int(input("Enter your friend age: "))
print(name1,age1,sep="\n")