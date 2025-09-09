a=int(input("Enter 1st side :"))
b= int(input("Enter 2nd side :"))
c=int(input("Enter 3d side :"))

if(a<90 and b<90 and c<90):
    print("It is an acute triangle")
elif(a==90 or b==90 or c==90):
    print("It is an right angled triangle")

else:
    print("It is an abuse triangle")