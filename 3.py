#1
# n=int(input("Please enter number : "))
# x=n**2
# for i in range(1,x):
#     if(x%i==0):
#         print("square of ",n,"not prime.")
#         break
#     else:
#         print("square of ",n,"prime")

#2
# n=int(input("Please input terms : "))
# print("a :")
# for i in range(1,n+1,3):
#     print(i)
# print("b :")
# j=0
# for i in range(1,n+1,3):
#     j=j+1
#     if(j%2==0):
#        print(-i)
#     else:
#         print(i) 

#3
# n1=float(input("Please enter side 1 : "))
# n2=float(input("Please enter side 2 : "))
# n3=float(input("Please enter side 3 : "))
# if(n1==n2==n3):
#     print("triangle is equilateral")
# elif(n1==n2 or n1==n3 or n2==n3):
#     print("triangle is isosceles")
# else :
#     print("triangle is scalene.")

#4
# n1=int(input("Please enter number 1 : "))
# n2=int(input("Please enter number 2 : "))
# n3=int(input("Please enter number 3 : "))
# if((n1>n2 and n1<n3)or(n1>n3 and n1<n2)):
#     print("the second largest number : ",n1)
# elif((n2>n1 and n2<n3)or(n2>n3 and n2<n1)):
#     print("the second largest number : ",n2)
# elif((n3>n1 and n3<n2)or(n3>n2 and n3<n1)):
#     print("the second largest number : ",n3)

#5
n=int(input("Please enter terms : "))
k1=0
k2=1
ans=1
for i in range(1,n):
    if(n==1):
        print("0")
        break
    elif(n==2):
        print("0\n1")
        break
    else:

        ans=ans+k2
        k2=ans
        k=k+i
        print(ans)
ans=k+i

#7
n=int(input("Please input n :"))
ans=1
for i in range(1,n+1):
    ans=i*ans
print(ans)
#8
# n=int(input("Please enter n: "))
# for i in range(1,n+1):
#     print("*"*i)
# for i in range(1,n+1):
#     print("*"*(n-i))