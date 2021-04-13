data = {}
name = input("Enter name: ")
password = input("Enter password: ")
if name in data:
    print("User Already exists")
else:
    data.update({name:password})
    print("User added")
name = input("Enter name: ")
password = input("Enter password: ")
if name not in data:
    print("User not found")
else:
    if password == data[name]:
        print("Authenticated!!!")
    else:
        print("Not Authenticated")