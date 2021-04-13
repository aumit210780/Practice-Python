''''
def printer(value):
    print(value.upper())
    
def wrapper(func):
    func("hello")
wrapper(printer)
'''
def wrapper(func):
    print("I am the decorator function")
    func("hello")
    
@wrapper
def printer(value):
    print("I am printed after")
    print(value.upper())
