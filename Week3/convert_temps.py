def C_to_F(var):
    F=var*1.8+32
    return(F)

def F_to_C(var):
    C=(var-32)/1.8
    return(C)

def main():
    loop=True
    line=0
    File=open('temps_input.txt','r')
    File2=open('temps_output.txt','w')
    while loop!=False:
      C_OR_F="F"
      if (C_OR_F=="C"):
          try:
              number=float(File.readline())
              number=C_to_F(number)
              print(number,file=File2)
          except ValueError:loop=False
      elif (C_OR_F=="F"):
          try:
              number=float(File.readline())
              number=F_to_C(number)
              print(number,file=File2)
          except ValueError:loop=False

    print("Fin")
    File.close()
    File2.close()

if __name__ == '__main__':
    main()