num1=int(input("Enter 1: "))
num2=int(input("Enter 2: "))
num3=int(input("Enter 3: "))

if (num1>num2 and num1>num3):
    print("Num 1 is greatest",num1)
elif(num2>num1 and num2>num3):
    print("Num 2 is greatest",num2)
else:
    print("Num 3 is greatest",num3)