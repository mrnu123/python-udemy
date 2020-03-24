# 1
# def check(s):
#     if s=="palindrome":
#         print("yes")
#     else:
#         print("no")

# s=input("Enter string : ")
# check(s)

# 2
# def mail(id):
#     if "@google.com"==id[-11:]:
#         print("yes")
#     else:
#         print("no")
# s=input("Enter E-mail ID : ")
# mail(s)

#3
# def maxchar(s):
c=[["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
print(c[1])


# 4
# def phone(num):
#     d=0
#     if len(num)==12 and num[3]=="-" and num[7]=="-":
#         for i in range(0,len(num)):
#             if num[i].isdigit():
#                 d=d+1
#             else:
#                 continue
#         if(d==10):
#             print("Valid.")
#         else:
#             print("Not valid.")
#     else:
#         print("Not valid.")
# p=input("Enter phone number : ")
# phone(p)

# 5
# def check(s):
#     sum=0
#     cd=0
#     k=0
#     d=[]
#     for i in range(0, len(s)):
#         if(s[i].isdigit()):
#             cd=cd+1
#             sum=sum+int(s[i])
#             d.append(int(s[i]))   
#         else:
#             continue
#     if(cd==0):
#         print(s," has no digits.")
#     else:
#         print(s,"\n digit = ",d,"\n sum of digits = ",sum)

# s1=input("Enter string: ")
# check(s1)

#6
# def percent(s):
#     d=0
#     st=0
#     for i in range(0,len(s)):
#         if(s[i].isdigit()):
#             d=d+1
#         else:
#             st=st+1
  
#     if d==0:
#         l=1
#         k=0
#         for i in range(1,len(s)+1):
#             l=l*i;
#         print("character = ",st/len(s)*100,"%")
#         print("numeric = 0%")
#         print("All case swap character :")
#         m=len(s)
#         s=s*2
#         n=s[::-1]
#         j=0
#         for i in range(0,m):
#             print(i+1,") ",s[i:m+i])
#         for i in range(m,len(n)):
#             print(i+1,") ",n[j:m+j])
#             j=j+1
#     else:
#         print("character = ",st/len(s)*100,"%")
#         print("numeric = ",d/len(s)*100,"%")
# s=input("Enter string : ")
# percent(s)

# 7
# def st(s):
#     k=len(s)
#     for r in range(0,(len(s)//2)):
#         k=k-2
#         print(" "*r,s[r]," "*(k),s[-1-r])
#     print(" "*(len(s)//2+1),s[(len(s)//2)])
# s1=input("Enter string1 : ")
# s2=input("Enter string2 : ")
# print(s1)
# st(s2)

# 8
# def sumString(s):
#     sum=0
#     for i in range(0,len(s)):
#         if s[i].isdigit():
#             sum=sum+int(s[i])
#         else:
#             continue
#     print(sum)
# s=input("Enter digits : ")
# sumString(s)

# 9
# def dictionary(s1,s2):
#     if s1<s2:
#         print(s1)
#     else:
#         print(s2)
# s1=input("Enter string 1 : ")
# s2=input("Enter string 2 : ")
# dictionary(s1,s2)
