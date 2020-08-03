def main():
    Name=input("Enter name:")
    loop=0
    while loop==0 :
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit")

        reload=0
        while reload==0:
            x=input()
            x=x.upper()
            if(x!="H") and (x!="G") and (x!="Q"): print("Invalid choice")
            else: reload=1

        if(x=="Q") :
            print("Finished.")
            loop=1
        elif(x=="H") :
            print("Hello ",Name)
        elif(x=="G") :
            print("Goodbye ",Name)




main()