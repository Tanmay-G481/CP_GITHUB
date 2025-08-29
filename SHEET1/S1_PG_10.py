numm= int(input("Enter nnumber"))
dict = {1:"monday",2:"Tueaday",3:"wednesday",4:"Thrusday",5:"friday",6:"Saturday",7:"Sunday"}
if(numm>=1 and numm<=7):
    for i in dict:
        if i==numm:
            print(dict[i])