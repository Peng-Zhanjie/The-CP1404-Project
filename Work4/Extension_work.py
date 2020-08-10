def Enter_string():
    Record=[]
    Loop=True
    Reenter=[]
    while Loop==True:
        Append=True
        string=input("Please enter a string:")
        if(string==""):
            Loop=False
            break
        for char in Record:
            if(string==char):
                Append=False
                if string not in Reenter:Reenter.append(string)
        if(Append!=False):Record.append(string)
    print("Valid String:")
    for chart in Record:
        print("[{}]".format(chart),end=' ')
    print()
    for newchart in Reenter:
        print("Strings repeated: [{}]".format(newchart))

def add_memberwise():
     print("Here is the function of add two List:")
     List1=[1,2,3,4,5]
     List2=[3,4,5]
     Length1=len(List1)
     Length2=len(List2)
     print("List1:",List1)
     print("List2:",List2)
     if(Length1==Length2):
        List3=[]
        for i in range(Length1):
            List3.append(List1[i]+List2[i])
     elif (Length1>Length2):
        List3 = []
        for i in range(Length2):
            List3.append(List1[i] + List2[i])
        for j in range(Length2,Length1):
            List3.append(List1[j])
     elif (Length1<Length2):
        List3 = []
        for i in range(Length1):
            List3.append(List1[i] + List2[i])
        for j in range(Length2,Length3):
            List3.append(List1[j])
     print("The add of two List is:",List3)



Enter_string()
add_memberwise()