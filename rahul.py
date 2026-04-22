print("Hello World")
#type Conversion in python..

mytuple = ("apple", "banana", "cherry")
mylist = list(mytuple)
mylist[1] = "kiwi"
mytuple = tuple(mylist)

print(type(mytuple))
print(mytuple)
