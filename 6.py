import math
import statistics 

# 1
# n=int(input("Enter n: "))
# num=[]
# for i in range(n):
#     num.append(int(input("Enter number: ")))
# print("mean of a list number ",num," is ",sum(num)/n)

# 2
# n=int(input("Enter n: "))
# num=[]
# for i in range(n):
#     num.append(int(input("Enter number: ")))
# key=int(input("Enter number for count frequency : "))
# print("Frequency of ",key," is ",num.count(key))

# 3
# n=int(input("Enter n: "))
# num=[]
# for i in range(n):
#     num.append(int(input("Enter number: ")))
# print("Frequency of a given number in a ",num," : ")
# for x in range(n):
#     y=num[0]
#     if x==0:
#         y=num[x]
#         print(y," : ",num.count(y))
#     else:
#         if num[x]==y:
#             continue
#         else:
#             y=num[x]
#             print(y," : ",num.count(y))

# 4
# n=int(input("Enter n: "))
# num=[]
# for i in range(n):
#     num.append(int(input("Enter number: ")))
# num.reverse()
# print("Reverse of list : ",num)

# 5
# n1=int(input("Enter n1: "))
# num1=[]
# num2=[]
# for i in range(n1):
#     num1.append(int(input("Enter number: ")))
# n2=int(input("Enter n2: "))
# for i in range(n2):
#     num2.append(int(input("Enter number: ")))
# print("3rd list : ",num1+num2)

# 6
# n = int(input("Enter n: "))
# num = []
# for i in range(n):
#     num.append(int(input("Enter number: ")))
# print(num[-1])
# for i in range(n-1):
#     print(num[i])

#7
# n=int(input("Enter n : "))
# str_l=[]
# str_min="a"
# str_max="b"
# max=0
# for i in range(n):
#     s=input("input string : ")
#     str_l.append(s)
#     str_tuple=tuple(str_l)
# min=len(str_tuple[0])
# for i in range(len(str_tuple)):
#     if (len(str_tuple[i])<=min):
#         min=len(str_tuple[i])
#         str_min=str_tuple[i]
#     if (len(str_tuple[i])>max):
#         max=len(str_tuple[i])
#         str_max=str_tuple[i]
# print("Maximum string : ",str_max)
# print("Minimum string : ",str_min)

#8
# n=int(input("Enter n: "))
# num=[]
# mean=[]
# sd=[]
# num_tuple=("")
# for i in range(n):
#     n_ele=int(input("Enter n of element : "))
#     for j in range(n_ele):
#         num.append(int(input("Enter number: ")))
#     num_tuple=tuple(num)
#     mean.append(sum(num_tuple)/len(num_tuple))
#     sd.append(statistics.stdev(num_tuple))
# print("mean : ",mean)
# print("SD : ",sd)
#9
# n=int(input("Enter number of pairs : "))
# rec=[]
# for i in range(n):
#     a=int(input("a: "))
#     b=int(input("b: "))
#     if (a%2==1 and b%2==1):
#         rectu=(a,b)
#         rec.append(rectu)
# print(rec)

#10
# n=int(input("Enter number of students : "))
# score=[]
# for i in range(n):
#     s1=float(input("Enter score of subject 1 for student number %d : "%(i+1)))
#     s2=float(input("Enter score of subject 2 for student number %d : "%(i+1)))
#     s3=float(input("Enter score of subject 3 for student number %d : "%(i+1)))
#     score_tuple=(s1,s2,s3)
#     score.append(sum(score_tuple)/3)
# for i in range(n):
#     print("Student number ",i+1," has Avg score : ",score[i])

#11
# num1=[]
# num2=[]
# for i in range(2):
#     n=int(input("Enter n of number : "))
#     for j in range(n):
#         if i==1:
#             num1.append(int(input("Enter number : ")))
#         else:
#             num2.append(int(input("Enter number : ")))
# print(set(num1).issubset(num2))

