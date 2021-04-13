def forone():
    print("First Choice")
def fortwo():
    print("Second Choice")

menu = {1:forone,2:fortwo}
choice = int(input("Enter 1 for first\nEnter 2 for second\n"))
if choice in menu:
    menu[choice]()
else:
    print("Wrong Input")