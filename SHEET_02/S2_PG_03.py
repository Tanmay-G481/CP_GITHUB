# QUES-03
    # print all even numbers from 1 to N, where you have to take N as input:

    # from the user.
    # Input:- N = 10
    # Output:- 2 4 6 8 10

# CODE/-

num1 = int(input("Enter number to print even number upto number entered: "))

for i in range(1,num1+1):
    if(i%2==0):
        print(i,end=" ")
print()