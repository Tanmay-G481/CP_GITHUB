ch =int(input("Enter no. of int to store:"))
l1 =[]
avg=0
for i in range(ch):
    a=int(input("Enter number: "))
    l1.append(a)

    res = sum(l1)/ len(l1)
    print("Avg is", res)