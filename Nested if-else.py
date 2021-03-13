CODE = "ASDFGHJ"
PASSWORD1 = "hello"
PASSWORD2 = "world"
EMAIL = "hello.python@gmail.com"

password1 = input("Enter PASSWORD1: ")
email = input("Enter EMAIL: ")

if PASSWORD1 == password1 and EMAIL == email:
    print("Level 1 access granted....(:")
    print()
    password2 = input("Now enter PASSWORD2: ")
    if(password2 == PASSWORD2):
        print("Welcome!!!!! The Security code is : ",CODE)
        print()
    else:
        print("PASSWORD2 is invalid!!!!!!!")
        print()
else:
    print("Invalid Data !!!!!! Sorry....):")
    print()