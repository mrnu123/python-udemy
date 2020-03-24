#1
# def factorial(num):
#     sum=1
#     for i in range(1,num+1):
#         sum=sum*i
#     return sum

# n1=int(input("Please enter number : "))
# print("factorial of ",n1," is ",factorial(n1))

#2
# def sum_num(*nums):
#     sum=0
#     for n in nums:
#         sum=sum+n
#     return sum

# print("Sum of all digits is ",sum_num(5,6,7))

#3
# def prime(n):
#     for i in range(2,n):
#         if(n%i==0):
#             return False
#         else:
#             return True

# num=int(input("Please enter number : "))
# print(num," ",prime(num))

#5
# def simpleinterest(p,r,t):
#     s=(p*r*t)/100
#     return s
# p=float(input("Please enter principal amount : "))
# r=float(input("Please enter rate: "))
# t=float(input("Please enter time: "))
# print("Simple interest = ",simpleinterest(p,r,t))

#6
# def ctof(c):
#     f=1.8*c+32
#     return f
# c=float(input("Please enter Celsius value :"))
# print(c," Celsius = ",ctof(c)," Fahrenheit")

#7
# def hi():
#     print("Hello python")

# hi()

#8
# def SayHiUser(name):
#     print("Hello ",name)

# name=input("Please enter your name: ")
# SayHiUser(name)

#9
# def hi():
#     name="User"
#     return name

# print("Hello ",hi())

#10
# def odd_even(num):
#     if (num%2==0):
#         return "even"
#     else:
#         return "odd"

# num=int(input("Please enter number : "))
# print(num, "is ",odd_even(num))