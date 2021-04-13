'''
def wrapper(string):
    def clean(name):
        print(string.upper(),name)
    return clean # or print(clean())
a = wrapper("Programming")
a("Raj")
'''
def n_mux(a):
    def answer(b):
        print(a*b)
    return answer
print(n_mux)
a= n_mux(5)
a(8)
b= n_mux(3)
b(8)