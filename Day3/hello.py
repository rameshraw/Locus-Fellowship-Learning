# # print format
# print("hello",'world',"'I am programmer",sep='!')
# print("Welcome to my world\n"*10)
# #input
# a=input("Enter the ");
# print(type(a))
# print(a)
# # f string
# print(f"The value of number a = {a}")
# b=int(input("enter the number:"))
# print(type(b))

# conditional statements
# age=int(input("enter your age:"))
# if (age>=18):
#     print("Adult")
# elif(age<0):
#     print("Age cannot be negative")
# else:
#     print("Not adult")
# # shorthand if else
# age="adult" if a>=18 else "not adult"

# for loop
# for i in range(6):
#     print(i)
# # while loop
# x=10
# while x>=0:
#     print(x)
#     x-=1

# functions
# def personal():
#     name=input()
#     phone=input()
#     address=input()
#     age=input()
#     print(name,phone,address,age)

# personal()

# def add(a,b=7):
#     # print(a+b)
#     return a+b

# print(add(7))

# list

# list =[1,3,5,7,9]
# list2=[1,"Ramesh Rawal",15,"csit"]
# print(list)
# print(list[-1])
# print(list2[:])
# print(min(list))
# print((max(list)))
# print(len(list))
# list.sort()
# print(list)
# list.reverse()
# print(list)
# print(sorted(list))
# dictionary
# d={
#     "first":"Rahul",
#     "second":"Syam"
# }
# print(d["first"])

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Name:{self.name}  Age:{self.age}")

p1=Person("Ramesh",20)
# p3=Person()
# print(p3)
p2=Person("Ramesh",20)
p1.greet()
# print(p1==p2)
