A=[1,2,3,4]
Even_A = 0
Odd_A = 0
for i in range(len(A)):
    if(A[i]%2==0):
        Even_A+=1
    else:
        Odd_A+=1
result = Even_A - Odd_A
print(f"Absolute difference is: {result}")

# output:

# Absolute difference is: 0