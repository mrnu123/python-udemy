# 1
# year = int(input("Enter year : "))
# if (year % 4 == 0 and year % 100 != 0):
#     print("leap year.")
# elif(year % 100 == 0 and year % 400 == 0):
#     print("leap year.")
# else:
#     print("not leap year")

# 2
# num=int(input("enter number : "))
# while num!=0:
#     print(num%10)
#     num=num//10

# 3
# num = input("Enter 3 number : ")
# max=num[1]
# for i in range(1, 3):
#     if(num[i]>max):
#         max=num[i]
# print(max)

# 4
# num=int(input("Enter number : "))
# if(num>0):
#     print("positive")
# elif(num==0):
#         print("zero")
# else:
#     print("negative")

# 5
# num = input("Enter 3 number : ")
# sum1 = 0
# sum2 = 0
# num1 = int(num)
# sum1 = (num1 % 10)+((num1//10) % 10)+(num1//100) % 10
# print("sum1 : " ,sum1)
# if(num[0] != num[1] and num[1] == num[2]):
#     num1 = int(num)
#     num1 = num1//10
#     sum2 = (num1 % 10)+((num1//10) % 10)
#     print("sum2 : ",sum2)
# elif(num[1] != num[2] and num[0] == num[2]):
#     num1 = int(num)
#     num1 = num1//10
#     sum2 = (num1 % 10)+((num1//10) % 10)
#     print("sum2 : ", sum2)
# elif(num[0] != num[2] and num[0] == num[1]):
#     num1 = int(num)
#     num1 = num1 % 100
#     sum2 = (num1 % 10)+((num1//10) % 10)
#     print("sum2 : ",sum2)
# elif(num[0] == num[2] and num[0] == num[1]):
#     print("sum2 : there are duplicate.")
# else:
#     num1 = int(num)
#     sum2 = (num1 % 10)+((num1//10) % 10)+(num1//100) % 10
#     print("sum2 : ", sum2)

# 6
# num=int(input("Enter number : "))
# for i in range(2,num):
#     if(num%i==0):
#         print("not prime")
#         break
#     else:
#         print("prime")
#         break

# 7
# num=input("Enter number : ")
# for i in range(1,len(num)):
#     if(num[i])

# 8
num = input("enter number : ")
j = 0
min = num[0]
int x =len(num)
while (x!=0):
    for i in range(1, len(num)):
        if(num[i] < min):
            min = num[i]
            j=i;
    print(min)
    x=x-1
# 9
# row = int(input("Enter row of table : "))
# column = int(input("Enter column of table : "))
# for i in range(1, row+1):
#     print("---"*column)
#     print("|  "*(column+1))
# print("---"*column)


# 10
# n=int(input("Enter n : "))
# sum=((1+n)*n)/2
# print(sum)

# 11
# even=0
# odd=0
# n=int(input("Enter n : "))
# for i in range(1,n+1):
#     if(i%2==0):
#         even=even+i
#     else:
#         odd=odd+i
# print("even = ",even)
# print("odd = ",odd)

# 12
# n = int(input("enter n : "))
# for i in range(1, n+1):
#     print("*"*n)
#     n = n-1
