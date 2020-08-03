def ASCLL():
    char=input("Please enter a char: ")
    x=ord(char)
    #char=chr(x)
    print("The ASCLL of",char,"is {}".format(x))
    jug=True
    while jug!=False:
        try:
            Code=int(input("Enter a number between 33 and 127:"))
            if (Code>127) or (Code<33): print("Invalid number")
            else:jug=False
        except ValueError: print("ValueError")
    y=chr(Code)
    print("The char of ASCLL {}".format(Code),"is",y)
    for i in range(33,128):
        print("{:>3}".format(i)," ",chr(i))



ASCLL()