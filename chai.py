# print('hello Chai')
# for i in range(1, 6):
#     for j in range(i):
#         print("*",end="")
#     print()

# ###########################
# i = 1 
# while (i<=5):
#     j = 1
#     while (j<=i):
#         print("*",end='')
#         j = j + 1
#     print()
#     i = i +1



# for i in range(1,6):
#     for j in range(i):
#         print("*",end='')
#     print()

# n = int(input("Enter Number: "))
# count=0
# i=1
# while(i<=n):
#     if(n%i==0):
#         count=count+1
#     i=i+1
# if(count==2):
#     print("Prime number")
# else:
#     print("composits Number")

class God:
    a = 1
    b = "ram"
    c = 1.25
    def __init__(self,name,age):
        self.a = name
        self.b = age
obj = God('rama',25)
print(obj.a," ",obj.b)
print(type(obj.c))
print(obj.a,obj.b)