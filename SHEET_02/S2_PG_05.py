# QUES-05

    # sum of all Natural numbers from 1 to N, where you have to take N as
    # input from user
    # Input:- N = 10
    # Output:- 55

# CODE/-

inp = int(input("Enter number:"))
sum=0
while(inp!=0):
    sum = sum+inp
    inp=inp-1
print(sum)