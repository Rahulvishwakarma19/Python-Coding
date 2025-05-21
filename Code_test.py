# def calulater(a=5,b=3):
#     print("add: ",a+b)
#     print("sub: ",a-b)
#     print("mul: ",a*b)
#     print("div: ",a/b)

# calulater(2,2)

# try:
#     a = 10
#     b = 0
#     print(a/b)

# except:
#     print("same error")
# else:
#     print("hello")
# finally:
#     print("jay shree ram")

# class A:
#     name = "ram"
#     age = 20
#     def __init__(self):
#         print(self.name," ",self.age)

#     def show(self):
#         print(self.name," ",self.age)

# obj = A()
# obj.show()

# f = float(input("Enter your hight: "))
# f=int(f)
# print("the hight is: ",f)
# print(type(f))

#print(round(2154.21424,2))
# name="Ram"
# age= 25
# hight=5.8
# print(f"My name is {name} and My age {age} and My hight{hight}")
# num=int(input("Enter the number: "))
# try:
#     if(num%2==0):
#         print(num,"Even number")
#     else:
#         print(num,"odd number")
# except:
#     print("The number is 0")

# total = 0
# men = int(input("Enter how many men come: "))
# hight = []
# for i in range(men):
#     x = int(input("Enter the hight of the men in miter: "))
#     total = total+x
#     hight.append(x)
    
# print(hight)
# print("Total of men hight: ",total)
# avg=total/men
# print("avrage of men is ",avg)

# num = int(input("Enter the lenth of number: "))
# list = []
# for i in range(num):
#     list_num=int(input("Enter the list number: "))
#     list.append(list_num)
    
# print(list)
# max_list = max(list)
# print("The max number in the list ",max_list)

# total = 0
# for i in range(1,101):
#     if i%2==0:
#         print("Even number",i)
#         total= total+i
# print("sum of Even number: ",total)

# import random
# letter = ['a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','N','O','P','Q','R','S','T','U','V','X','Y','Z']
# number = ['1','2','3','4','5','6','7','8','9','0']
# symbol = ['!','@','#','$','%','^','&','*','(',')','_','+']
# print("Wellcome to password genreter.")
# n_letter = int(input("Enter the lenth of the letter in password. "))
# n_number = int(input("Enter the lenth of the number in password. "))
# n_symbol = int(input("Enter the lenth of the symbol in password. "))
# password = ""
# for i in range(1,n_letter+1):
#     char = random.choice(letter)
#     password = password + char
# for i in range(1,n_number+1):
#     char = random.choice(number)
#     password = password + char
# for i in range(1,n_symbol+1):
#     char = random.choice(symbol)
#     password = password + char
# print(password)

# sum_p = 0
# sum_n = 0
# num = int(input("Enter the number or you whant exite pares 0 :"))
# while num !=0:
#     if(num>0):
#         sum_p = sum_p + num
#     else:
#         sum_n = sum_n + num
#     num = int(input("Enter the number or you whant exite pares 0 :"))
    
# else:
#     print("loop will end now..")
#     print("Sum of positive number: ",sum_p)
#     print("Sum of nagative number: ",sum_n)

# count = 0
# number = int(input("Enter the number: "))
# while(count <= 10):
#     table = number * count
#     print(count,"ekam",table)
#     count+=1

# def name(age,gender):
#     print("hello my name is rahul..")
#     print(age,"my age and my gender ",gender)

# name(16,"man")

#prime number  
# number = int(input("Enter the number: "))
# prime = True
# if(number==0 or number == 1):
#     print("not prime number..")
# else:
#     for i in range(2,number):
#         if(number%i==0):
#             prime = False
#     if(prime == True):
#         print("This is prime number..")
#     else:
#         print("This is not prime number..")

# class Food: 

#     def __init__(self,name="banana",price = 200):
#         self.name = name
#         self.price = price

#     def myfood(self):
#         print("this is food",self.name)

# obj = Food("mango",1000)
# obj.myfood()
# obj.price = 2000
# print(f"what is food name{obj.name}and what is the price{obj.price}")
# obj1 = Food("ram")
# obj.myfood()
# class Good(Food):
#     def good_food(self):
#         print("this food is very good")
# obj = Good()
# obj.good_food()


#print Prime number or composit number..
# n = int(input("Enter the number: "))  
# count = 0
# i = 1
# while(i<=n):
#     if(n%i==0):
#         count = count+1
#     i = i+1
# if(count == 2):
#     print("the number is Prime")
# else:
#     print("the number Composit")

# student_marks ={
#     "Janny":92,
#     "Harry":78,
#     "Dimpy":56,
#     "Rahul":41,
#     "Aniket":99,
#     "Prem":35
# }
# student_gread={}
# for student in student_marks:
#     marks=student_marks[student]
#     if(marks>90):
#         student_gread[student]="A+"
#     elif(marks>80):
#         student_gread[student]="A"
#     elif(marks>70):
#         student_gread[student]="B+"
#     elif(marks>60):
#         student_gread[student]="B"
#     elif(marks>50):
#         student_gread[student]="C"
#     elif(marks>40):
#         student_gread[student]="D"
#     else:
#         student_gread[student]="F"
# print(student_gread)

# def add(a,b):
#     c=a+b
#     return c

# print(add(14,6))
# total = add(14,6)
# print(total)

# a = 10# global
# def display():
#     a = 15# local
#     print(a)

# display()

# class Male:
#     def work(self):
#         print("Hard work..")
# class Female (Male):
#     def work(self):
#         super().work()
#         print("hee..")

# obj = Female()
# obj.work()

# class University:
#     def book(self):
#         print("This is University book..")
# class Course (University):
#     def book(self):
#         super().book()
#         print("This is Course book..")
# class Branch (University):
#     def book(self):
#         super().book()
#         print("This is Branch book..")
# class Student (Course,Branch):
#     def book(self):
#         super().book()
#         print("This is Student book..")
# class Faculty (Branch):
#     def book(self):
#         super().book()
#         print("This is the Faculty book..")
# obj1= Faculty()
# #print(Faculty.mro()) #how to now the step of the class function call..
# obj1.book()
# print("next object line..")
# obj2= Student()
# obj2.book()

# class Parent:
#     def show(self):
#         print("I am dady..")
# class Chaild1(Parent):
#     def show(self):
#         super().show() 
#         print("I am son")
# class Chaild2(Parent):
#     def show(self):
#         super().show() 
#         print("I am doter")
# class Chaild3(Chaild1,Chaild2):
#     def show(self):
#         super().show() 
#         print("I am boy.. ")
# ch= Chaild3()
# ch.show()

File = open("data.txt","a+")
#File.write(" hii ..")
File.seek(0)
print(File.read())
File.write("good good")
File.close()