a = int(input("Enter a number: "))
print("Even/odd in multiple lines>>>>")
if a%2 == 0:
    print(a,"number is even")
else:
    print(a,"is odd")
    
print("Even" if a%2==0 else "Odd")
print("Even") if a%2==0 else print("Odd")