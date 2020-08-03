def Get_Number():
    jug=True
    while jug!=False:
        try:
            Code=int(input("Enter a number between 33 and 127:"))
            if (Code>127) or (Code<33): print("Invalid number")
            else:jug=False
        except ValueError: print("Please enter a Number!")
        return Code

def ASCLL():
    Code=Get_Number()
    y=chr(Code)
    print("The char of ASCLL {}".format(Code),"is",y)

ASCLL()