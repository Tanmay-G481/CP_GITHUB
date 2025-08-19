# QUES-01
    # Takes a positive integer N as input from the user and prints all natural numbers

    # numbers from 1 to N, with each number followed by a space.

    # Input:- N = 5
    # Output:- 1 2 3 4 5

# CODE/-

# N  = int(input("Enter number to prints all natural numbers : "))

# for i in range(1,N+1):
#     print(i)

# QUES-02
    # Print all Natural numbers from N to 1, where you have to take N as input

    # from the user.
    # Input:- N = 5
    # Output:- 5 4 3 2 1

# CODE/-

# num = int(input("Enter number to print all number till 1:"))

# for i in range(1,num+1):
#     print(num)
#     num = num-1

# QUES-03
    # print all even numbers from 1 to N, where you have to take N as input:

    # from the user.
    # Input:- N = 10
    # Output:- 2 4 6 8 10

# CODE/-

# num1 = int(input("Enter number to print even number upto number entered: "))

# for i in range(1,num1+1):
#     if(i%2==0):
#         print(i,end=" ")
# print()


# QUES-04

    # o print all odd numbers from 1 to N, where you have to take N as input.

    # from user.
    # Input:- N = 10Output:- 1 3 5 7 9

# CODE/-

# num2 = int(input("Enter num to print its odd number: "))
# while(num2>0):
#     if(num2%3==0):
#         print(num2)
#     num=num-1


# QUES-05

    # sum of all Natural numbers from 1 to N, where you have to take N as
    # input from user
    # Input:- N = 10
    # Output:- 55

# CODE/-

# inp = int(input("Enter number:"))
# sum=0
# while(inp!=0):
#     sum = sum+inp
#     inp=inp-1
# print(sum)
    


# QUES-06

    # Given an integer A, you need to find and return the sum of all the even numbers
    # between 1 and A. Even numbers are those numbers that are divisible by 2.
    # Input:- A = 5
    # Output:- 6
    # Explanation:- Even numbers between [1, 5] are (2, 4)

# CODE/-

# even=int(input("Enter number to calculate sum of all even number upto the number entered: "))

# sum_of_even = 0

# for i in range(even):
#     if(i%2==0):
#         sum_of_even = sum_of_even + i
# print(sum_of_even)



# QUES-07

    # Integer A as input. You have to print the sum of all odd numbers in the range [1,
    # A].
    # Input:- A= 4
    # Output:- 4
    # Explanation:- For A = 4, Odd numbers 1 and 3 lie in the range [1, 4]. Sum = 1 + 3 = 4

# CODE/-

# ODD=int(input("Enter number to calculate sum of all ODD number upto the number entered: "))

# sum_of_ODD = 0

# for i in range(ODD):
#     if(i%2!=0):
#         sum_of_ODD = sum_of_ODD + i
# print(sum_of_ODD)



# QUES-08


    # Take an integer N as input and print the count of digits of that number.
    # Input:- N = 10101
    # Output:- 5
    # Explanation:- 10101 has 5 digits

# CODE/-


# num =int(input("Enter no. to count length: "))

# count= 0
# for i in range(num):
#     # print(i)
#     pass
# print(count)

# QUES-09
    # Take an integer N as input. Your task is to calculate and print the sum of the digits of the
    # given number N.
    # Input:- N = 1589
    # Output:- 23
    # Explaination:- For the number 1589, the digits are 1,5,8,9. The Sum(1589) = 1+5+8+9 = 23

# CODE/-





# CLASS

# inn = int(input("Enter an integer: "))

# for i in range(1,inn+1,2):
#         print(i)


