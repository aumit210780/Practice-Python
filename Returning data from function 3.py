def clear_data(string):
    return string.strip()
print(clear_data(" hello "))

def square_of_listt(marks):
    res = []
    for each in marks:
        res.append(each**2)
    return res
print(square_of_listt([1,2,3,4,5]))

def sample(a,b):
    return a**2,b**2
a,b = sample(5,6)
print(a,b)

def names():
    return {"name":"brian","age":22}
data = names()
print(data["name"])    
        