#1
# c=float(input("Please enter temperature in Celsius : "))
# f=1.8*c+32
# print(c," Celsius = ",f," Fahrenheit")

#2
# num=5
# print(num)
# print(num*2)
# print(num*2-1)

#3
# r=float(input("Please input radius of a circle : "))
# print("Radius : ",r,"==> Area : ",3.14*r*r)

#4
# mark1=float(input("Please input mark of subject 1 : "))
# mark2=float(input("Please input mark of subject 2 : "))
# mark3=float(input("Please input mark of subject 3 : "))
# mark4=float(input("Please input mark of subject 4 : "))
# mark5=float(input("Please input mark of subject 5 : "))
# print("Average marks : ",(mark1+mark2+mark3+mark4+mark5)/5)

#5
# num1=float(input("Please input number 1 : "))
# num2=float(input("Please input number 2 : "))
# temp=num1
# num1=num2
# num2=temp
# print("Swap number ",num1," ",num2)

#6
# num1=float(input("Please input number 1 : "))
# num2=float(input("Please input number 2 : "))
# num1,num2=num2,num1
# print("Swap number ",num1," ",num2)

#7
# height_cm=float(input("Please input your height in cms : "))
# print(height_cm," cms. = ",height_cm/30.48," feet = ",height_cm*0.3937," inch")

#8
# P=float(input("Please input principle : "))
# i=float(input("Please input interest rate : "))
# n=float(input("Please input term of the loan : "))
# simple=P*i*n
# compound=P*(((1+i)**n)-1)
# print("Simple interest : ",simple)
# print("Compound interest : ",compound)

#9
# n=int(input("Please input number : "))
# n1=(n+1)*10
# n2=(n+2)
# n=n*100
# ans=n+n1+n2
# print(ans)

#10
# name=input("Please input your name : ")
# print("Welcome ",name)

#11
# sec=int(input("Please input number of seconds : "))
# hr=int(sec/3600)
# min=int(sec/60-60*hr)
# sec=int(sec-(3600*hr+60*min))
# print(hr," : ",min," : ",sec)

#12
num1=float(input("Please input number 1 : "))
num2=float(input("Please input number 2 : "))
num3=float(input("Please input number 3 : "))
num4=float(input("Please input number 4 : "))
num5=float(input("Please input number 5 : "))
print("The multiple is ",num1*num2*num3*num4*num5)