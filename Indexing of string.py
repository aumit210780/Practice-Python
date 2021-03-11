#Indexing of String
a = "Hello"
"""
H e l l o
0 1 2 3 4
-5-4-3-2-1
"""
print(a[3])
print(a[-4])
#String is immutable you can't do: a[0] = "O"
#a[0] = "O"
print(a)
a = "World"
print(a)