# li=[12,12,14,15,15,1471,148,135,1455]
# len(li)
# print(len(li))
# print(max(li))
# print(min(li))
# li.append(255)
# print("count karega kis plas pe hai:",li.count(12))
# print("give the index: ",li.index(148))
# print(li.insert(1,456))
#li.remove(12)#give first given object ko delete kar deta hai.
#print(li)
# li.sort()# asending order me kar deta hai
# li.sort(reverse=True)# desending order me kar deta hai
# print(li)
# print(li)
# print(li.pop())#last ka object delete kar deta hai
# li.extend([114,58,69,78])#last me add kar deta hai multipal list
# print(li)

# li=[12,12,14,15,15,1471,148,135,1455]
# li.sort()
# li.sort(reverse=True)
# li.append(19)
# li.insert(5,55)
# li.remove(55)
# li.pop()
# print(li)

# num=int(input("Enter the number: "))
# i=1
# count=0
# while(i<=num):
#     if(num%i==0):
#         count=count+1
#     i=i+1
# if(count==2):
#     print("Prime number..")
# else:
#     print("complex number..")

# n=int(input("Enter the number: "))
# x=0
# y=1
# z=0
# while(z<=n):
#     print(z)
#     x=y
#     y=z
#     z=x+y

# class Home:
#     name='rahul'
#     age=12
# class Ho(Home):
#     def Fun(self):
#         print("hello I am rahul")
# obj=Ho()
# print(obj.name)
# obj.Fun()

num=int(input("Enter the number: "))
sum=0
i=1
while(num>=i):
    if(num%i==0):
        sum=sum+1
    i=i+1
if(sum==2):
    print(num,"prime numbar..")
else:
    print(num,"composit numbar..")
