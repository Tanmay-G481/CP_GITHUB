A =[1,2,3,4,5]
Even=[]
odd=[]
for i in range(len(A)):
    if A[i]%2==0:
        Even.append(A[i])
    else:
        odd.append(A[i])
print(*odd)
print(*Even)

# OUTPUT

# 1 3 5
# 2 4