# age = int(input("Enter age:"))

# if(age>=18):
#     print("Yes!!you are eligible")
# else:
#     print("Sorry!!")


# # 2.
# no = int(input("Enter number to check:"))

# if(no%7==0):
#     print("Yes no is divisible of 7")
# else:
#     print("No")

# # 3.If_Last_NoIS4

# digit =int(input("Enter number to check the last digit:"))
# if digit%3==0 and digit%10==4:
#     print("Yes")

# 5.
# A = int(input("Enter an integer:"))
# if(A%5==0 and A%11==0):
#     print("YES")
# else:
#     print("No")5


# # 6.
# num1=int(input("Enter 1: "))
# num2=int(input("Enter 2: "))
# num3=int(input("Enter 3: "))

# if (num1>num2 and num1>num3):
#     print("Num 1 is greatest",num1)
# elif(num2>num1 and num2>num3):
#     print("Num 2 is greatest",num2)
# else:
#     print("Num 3 is greatest",num3)


# # 7
# a=int(input("Enter 1st side :"))
# b= int(input("Enter 2nd side :"))
# c=int(input("Enter 3d side :"))

# if(a<90 and b<90 and c<90):
#     print("It is an acute triangle")
# elif(a==90 or b==90 or c==90):
#     print("It is an right angled triangle")

# else:
#     print("It is an abuse triangle")

# # 8.
# age = int(input("Enter age:"))

# if(age<18):
#     print("You are not eligible")
# else:
#     print("You are eligible")


# # 9.

# leap = int(input("Enter year:"))

# if leap%4==0:
#     print("YEs it is a leap year")
# else:
#     print("It is not an leap year")

# 10.

# numm= int(input("Enter nnumber"))
# dict = {1:"monday",2:"Tueaday",3:"wednesday",4:"Thrusday",5:"friday",6:"Saturday",7:"Sunday"}
# if(numm>=1 and numm<=7):
#     for i in dict:
#         if i==numm:
#             print(dict[i])
# 11.

# ch =int(input("Enter no. of int to store:"))
# l1 =[]
# avg=0
# for i in range(ch):
#     a=int(input("Enter number: "))
#     l1.append(a)

#     res = sum(l1)/ len(l1)
#     print("Avg is", res)


# 12.

# numb = int(input("Enter number for factor:"))
# i =1
# # fct = 1
# while i<=numb:
#     if(numb%i==0):
#         print(i)
#     i+=1

# 13.
ch = int(input("Enter numbers:"))
i =0
count = 0
while(ch>0):
    ch = ch//10
    count= count+1
print(count)