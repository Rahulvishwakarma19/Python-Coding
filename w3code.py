# class Home:
#     def __init__(self,name,age,mony):
#         self.name=name
#         self._age=age
#         self.__mony=mony
    
#     def __hous(self):
#         print(f"my{self.name}and{self._age}also i have {self.__mony}")
#     def yo(self):
#         self.__hous()

# obj = Home("Rahul",25,100000)
# print(obj.name)
# print(obj._age)
# print(obj.__mony)
# obj.yo()

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age

#     def get_age(self):
#         return self.__age
    
#     def set_age(self,age):
#         self.__age=age
    
#     def book(self):
#         print(f"my{self.name}and{self.__age}Yo..")

# obj=Student("ram",21)
# print(obj.name)
# print(obj.get_age())
# obj.set_age(25)
# print(obj.get_age())

# class Rahul:
#     num=int(input("Enter the Numbar: "))
#     i=1
#     count=0
#     while (i<=num):
#         if(num%i==0):
#             count=count+1
#         i=i+1
#     if(count==2):
#         print("The number is given is prime number")
#     else:
#         print("The number is composit number..")

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     print()
#     i=i+1
# print("for loop")
# for i in range (1,5+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(1,5+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# i=1
# while(i<=5):
#     b=1
#     while(b<=5-i):
#         print(" ",end=" ")
#         b=b+1
#     j=1
#     while(j<=i):
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1

# i =1
# while(i<=5):
#     j=1
#     while(j<=i):
#         print("*",end="")
#         j=j+1
#     print()
#     i=i+1

# print("This is for loop..")

# for i in range(1,5+1):
#     for j in range(i):
#         print("*",end="")
#     print()

u =['ram','shyam','narayan']
u.append("siv")
u.extend(["sita","parvati"])
print(u)

