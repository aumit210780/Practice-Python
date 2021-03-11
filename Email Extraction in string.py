"""
For Example here Email is : ooo345@gmail.com
and you have to print it separately like
ooo345
gmail
com
"""
email = input("Enter your email address here: ")
inofat = email.index("@")
inofdot = email.rindex(".")
print(email[:inofat])
print(email[inofat+1:inofdot])
print(email[inofdot+1:])