def main():
    saleprice=[0]
    reload=1
    while reload==1:
        looptime=int(input("Number of item: "))
        if(looptime>0): reload=0
        else: print(" Invalid number of items!")

    total=0
    for i in range(looptime):
        reloaditem=1
        while reloaditem==1:
            x=float(input("Price of item{}: ".format(i+1)))
            if(x<=0) : print(" Invalid number of items!")
            else: reloaditem=0
        saleprice.append(x)
        total=total+x
    print("Total price for {}".format(looptime),"items is ${:.2f}".format(total))

main()