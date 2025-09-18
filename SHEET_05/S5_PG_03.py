# 3.

A = [1,2,3,4,5]

max_A = A[0]
Min_A = A[0]

for i in range(1,len(A)):
    if(max_A<A[i]):
        max_A = A[i]
    if(Min_A>A[i]):
        Min_A=A[i]
print(f"MAX of the array is: {max_A}\nMin of the array is: {Min_A} ")

# OUTPUT

# MAX of the array is: 5
# Min of the array is: 1