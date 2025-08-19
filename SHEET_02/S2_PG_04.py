# QUES-04

    # o print all odd numbers from 1 to N, where you have to take N as input.

    # from user.
    # Input:- N = 10Output:- 1 3 5 7 9

# CODE/-

num2 = int(input("Enter num to print its odd number: "))
while(num2>0):
    if(num2%3==0):
        print(num2)
    num=num-1