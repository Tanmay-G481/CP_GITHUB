# QUES-06

    # Given an integer A, you need to find and return the sum of all the even numbers
    # between 1 and A. Even numbers are those numbers that are divisible by 2.
    # Input:- A = 5
    # Output:- 6
    # Explanation:- Even numbers between [1, 5] are (2, 4)

# CODE/-

even=int(input("Enter number to calculate sum of all even number upto the number entered: "))

sum_of_even = 0

for i in range(even):
    if(i%2==0):
        sum_of_even = sum_of_even + i
print(sum_of_even)