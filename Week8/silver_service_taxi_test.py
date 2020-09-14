from silver_service_taxi import SilverServiceTaxi

def main():
    """This program is modified version after Inheriting Enhancements"""

    Hummer=SilverServiceTaxi("Hummer",200,4)
    print(Hummer)
    print("fare={:.2f}".format(Hummer.get_fare()))
    Hummer.drive(100)
    print(Hummer)
    print("fare={:.2f}".format(Hummer.get_fare()))
    print()
    Taxi=SilverServiceTaxi("SilverServiceTaxi", 200, 2)
    print(Taxi)
    print("fare={:.2f}".format(Taxi.get_fare()))
    Taxi.drive(18)
    print(Taxi)
    print("fare={:.2f}".format(Taxi.get_fare()))


main()