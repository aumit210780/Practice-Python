a = "hello world!!!"
print(a.upper())
b = "HELLO WORLD!!!"
print(b.lower())
print(a.capitalize())

print(a.index("o")) #Print leftmost index of "o"
print(a.rindex("o")) #Print rightmost index of "o"
# print(a.index("@")) ;It will give error because @ is not present in the index 
print(a.find("o")) #It will print leftmost index of "o"
print(a.rfind("o")) #It will print rightmost index of "o"
print(a.find("@")) #It will give -1 as output because @ is not present in the string