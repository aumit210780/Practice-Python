def adder(a,b):
    return a+b
def mux(a,b):
    return a*b
add = adder
print(add(4,5))
print(adder(6,7))
print()
functions = [adder,mux]
print(functions[0](8,9))
print(functions[1](8,9))
