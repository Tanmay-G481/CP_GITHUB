n = int(input("enter rows: "))
nu= 1
for i in range(1, n+1):
    for j in range(i):
        print(nu, end=" ")
        nu += 1
    print()