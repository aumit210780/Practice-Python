dictt = {"tea":"beverage","coffee":"better beverage"}
print(dictt)
print(dictt["tea"])
print(dictt["coffee"])
# For adding new values in dictionary we use 'update' function
dictt.update({"soup":"nope","chips":"snacks"})
print(dictt)
#A dictionary can't have two same name key . If we use it, dictionary takes the last value of key as its updated value
dictt.update({"coffee":"not a better beverage","soup":"very healthy"})
print()
print(dictt)