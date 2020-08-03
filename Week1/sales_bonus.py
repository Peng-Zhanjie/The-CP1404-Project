def main():
    reload=1
    while reload!=0:
     sale=float(input("Enter you $: "))
     if sale >=0:
       if sale >= 1000:
          sale=sale*0.15
       else :
          sale=sale*0.1
       print("After the discount the prize is2 {}".format(sale))
     else:
         reload=0
         print("Finished ,thanks for your shopping.+")

main()