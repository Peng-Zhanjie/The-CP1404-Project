from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

def main():
    Taxi.price_per_km=1.2
    SilverServiceTaxi.price_per_km=1.2
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    returing = False
    bill = 0.0
    current_taxi = None
    print("Let's drive!")
    while returing is False:
        loop = True
        while loop is True:
            print("q)uit, c)hoose taxi, d)rive")
            choice = input(">>>")
            choice = choice.upper()
            if (choice == "Q") or (choice == "C") or (choice == "D"):
                loop = False
            else:
                print("Invalid choice")

        if choice == "C":
            print("Taxis available:")
            count = 0
            for tax in taxis:
                print("{} -".format(count),tax)
                count += 1
            loop1=True
            while loop1 is True:
                try:
                    number=int(input("Choose taxi: "))
                    if(number>=count):print("Invalid number")
                    else:
                        current_taxi=taxis[number]
                        print("Bill to date: ${:.2f}".format(bill))
                        loop1=False
                except ValueError:print("Invalid input")

        if choice == "D":
            if(current_taxi == None):print("You haven't chosen")
            else:
                loop2=True
                while loop2 is True:
                    try:
                        number_drive=int(input("Drive how far? "))
                        current_taxi.drive(number_drive)
                        bill=bill+current_taxi.get_fare()
                        print("Your {} trip cost you ${:.2f}".format(current_taxi.name,current_taxi.get_fare()))
                        print("Bill to date: ${:.2f}".format(bill))
                        loop2=False
                    except ValueError: print("Invalid input")


        if choice == "Q":
            returing=True
            print("Total trip cost: ${:.2f}".format(bill))
            print("Taxis are now:")
            countq=0
            for tax in taxis:
                print("{} -".format(countq), tax)
                countq += 1




main()
