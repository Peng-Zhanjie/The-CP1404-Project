Friend={"JoJo":4396}

def prints(Friend):
    loop=True
    while loop!=False:
        try:
            number=int(input("Please select a number to print:"))
            if(number<=0) or (number>len(Friend)):print("Invalid number")
            else:
                round=0
                for key in Friend.keys():
                    round+=1
                    if(round==number):
                        print("{}:{}".format(key,Friend[key]))
                loop=False
        except ValueError:print("Invalid input")

def change(Friend):
    loop=True
    while loop!=False:
        try:
            number=int(input("Please select a number to change:"))
            if(number<=0) or (number>len(Friend)):print("Invalid number")
            else:
                round=0
                for key in Friend.keys():
                    round+=1
                    if(round==number):
                        loop2=True
                        while loop2!=False:
                            Newnumber=input("Enter a new number for {}:".format(key))
                            if(Newnumber.isdigit()==False):print("Invalid number")
                            else:loop2=False
                        Friend[key]=Newnumber
                loop=False
        except ValueError:print("Invalid input")
def add(Friend):
    Name=input("Please enter a name:")
    loop = True
    while loop != False:
        Newnumber = input("Enter a number for {}:".format(Name))
        if (Newnumber.isdigit() == False):
            print("Invalid number")
        else:
            loop = False
    Friend[Name]=Newnumber

def  main():
    loop=True
    while loop==True:
        print("(P) print")
        print("(C) change")
        print("(A) add")
        print("(Q) quit")
        Choice=input(">>>").upper()
        if(Choice=="P"):prints(Friend)
        elif(Choice=="C"):change(Friend)
        elif(Choice=="A"):add(Friend)
        elif(Choice=="Q"):loop=False
        else:
            print("Invalid Choice")

main()