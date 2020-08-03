def main():
    x=int(input("Enter the x: "))
    y=int(input("Enter the y: "))
    for i in range(x,y):
        if(i%2==0): print(i,end=" ")
    print()
    for i in range(x, y):
        if (i % 2 != 0): print(i,end=" ")
    print()
    for i in range(x, y):
        for j in range(1,100):
            if(i==j*j):
                print(i,end=" ")
                break

main()