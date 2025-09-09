n=5

for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(2,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

    # OUTPUT

# * * * * * 
# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * *
# * * * * *

# Given an array compute the sum of all array

n = list(map(int,input("Enter: ").split()))
print(n)
# for i in (n)

# Given an array find the max value in it.
max = n[0]
for i in range(len(n)):
    if(n[i]>max):
        max=n[i]
print(max)#[1,2,3,4,5,6]


# Given an array and a target find number of occurance of target no in the array.

target = int(input("Enter target value: "))
cont=0
for i in range(len(n)):
    if(n[i]==target):
        cont+=1
print(cont)

# Given an array and  an increment number generate a nw array which contains all value of OG array increased by incerement value.

inc = int(input("enter incerement :"))
l2=[]
for i in range(len(n)):
    l2.append(n[i]+inc)
print(l2)

# Given an array generate a new array containing sq of all numbers

inc = int(input("enter incerement :"))
l3=[]
for i in range(len(n)):
    l3.append(n[i]*inc)
print(l3)

# Given an array filter put all odd numbers
