def printer(*args):
    print(args,type(args))
printer("Aumit",1,11.5)
print()
def printer(*args):
    for each in args:
        print(each, type(args))
printer("Aumit",1,11.5)
print()
def auth(**kwargs):
    print(kwargs)
auth(email = "temp123@gmail.com",password = "notrealpassword123")
print()
def auth(**kwargs):
    print("{} and {}".format(kwargs["email"],kwargs["password"]))
auth(email = "temp123@gmail.com",password = "notrealpassword123")
print()