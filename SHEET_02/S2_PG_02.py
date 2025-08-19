# QUES-02
    # Print all Natural numbers from N to 1, where you have to take N as input

    # from the user.
    # Input:- N = 5
    # Output:- 5 4 3 2 1

# CODE/-

num = int(input("Enter number to print all number till 1:"))

for i in range(1,num+1):
    print(num)
    num = num-1
