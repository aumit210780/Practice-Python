name = "Aumit Hasan"
print("First name is ",name[:5])
print("Last name is ",name[6:])

#A Pathway to print Firstname and lastname from any person fullname
name1 = input("Enter your name here: ")
spaceinname = name1.find(" ")
print("Your First name is ",name1[:spaceinname])
print("Your Lastname is ",name1[spaceinname+1:])