import random

data= "hello"
randomnumber = random.randint(0,len(data)-1)
print(data[randomnumber])

data = [1,2,3,4,5,6,9]
random.shuffle(data)
print(data)