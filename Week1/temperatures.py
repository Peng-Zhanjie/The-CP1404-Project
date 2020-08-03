def C_to_F(var):
    F=var*1.8+32
    return(F)

def F_to_C(var):
    C=(var-32)/1.8
    return(C)

def main():
    loop=True
    while loop!=False:
      C_OR_F=input("Please enter which kind temperature do you enter(C or F):")
      C_OR_F=C_OR_F.upper()
      if (C_OR_F=="C"):
          number=float(input("Enter a Celsius number here:"))
          number=C_to_F(number)
          loop=False
      elif (C_OR_F=="F"):
          number=float(input("Enter a Fahrenheit number here:"))
          number=F_to_C(number)
          loop=False
      else:
          print("invalid input.")
    if C_OR_F=="C":
        print("The result in Celsius is {:.4f}".format(number))
    elif C_OR_F=="F":
        print("The result in Fahrenheit is {:.4f}".format(number))
    print("Fin")

if __name__ == '__main__':
    main()