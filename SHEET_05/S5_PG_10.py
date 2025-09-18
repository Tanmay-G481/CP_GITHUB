# 10.

A=[3,5,1,2,1,2]
B=[]
for i in range(len(A),0,-1):
    B.append(A.pop())
print(B)

# OUTPUT:

# [2, 1, 2, 1, 5, 3]