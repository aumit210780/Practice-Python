string = input("Enter a string to check whether it is palindrome or not: ")
if string == string[::-1]:
    print(string,"is palindrome")
    print()
else:
    print(string, "is not palindrome")