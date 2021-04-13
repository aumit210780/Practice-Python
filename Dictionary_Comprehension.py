data = "helloworld"
dictt = {}
# h->'1',l->'3',o->'2'etc (these are frequency of each character)
for each in data:
    dictt.update({each:data.count(each)})
print(dictt)
print()
res = {each:data.count(each) for each in data}
print(res)