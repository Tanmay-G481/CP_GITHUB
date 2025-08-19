# QUES-07

    # Integer A as input. You have to print the sum of all odd numbers in the range [1,
    # A].
    # Input:- A= 4
    # Output:- 4
    # Explanation:- For A = 4, Odd numbers 1 and 3 lie in the range [1, 4]. Sum = 1 + 3 = 4

# CODE/-

ODD=int(input("Enter number to calculate sum of all ODD number upto the number entered: "))

sum_of_ODD = 0

for i in range(ODD):
    if(i%2!=0):
        sum_of_ODD = sum_of_ODD + i
print(sum_of_ODD)