n = int(input("Enter a number to play fuzz-buzz: "))
if n%3 == 0 and n%5 == 0:
    print("Fuzz-Buzz")
    print()
elif n%5 == 0:
    print("Buzz")
    print()
elif n%3 == 0:
    print("Fuzz")
    print()
else:
    print(n)
    print()