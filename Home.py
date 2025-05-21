# num = int(input("Enter the number: "))
# if(num%2==0):
#     print("the number is even")
# else:
#     print("the number is odd")

#Prime number
# count=0
# i=1
# num = int(input("Enter the number "))
# while(i<=num):
#     if(num%i==0):
#         count=count+1
#     i=i+1
# if(count==2):
#     print("the number is prime number..")
# else:
#     print("the number is composit number..")

#Factorial
# i=int(input("Enter the number: "))
# fac=1
# while(i>0):
#     fac=fac*i
#     i=i-1
# print("Factorial= ",fac)

#Cube
# i=int(input("Enter the number to find sum of cube : "))
# sum=0
# while(i>0):
#     sum=sum+(i%10)*(i%10)
#     i=i//10
# print("Sum of cube of each digits= ",sum)

count=0
i=1
n=int(input("Enter the number: "))
while(i<=n):
    if(n%i==0):
        count=count+1
    i=i+1
if(count==2):
    print("prime number.")
else:
    print("not prime number.")
