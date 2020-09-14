from taxi import Taxi


def main():
    """This program is modified version after Inheriting Enhancements"""

    taxi = Taxi(100, "Prius 1")
    taxi.drive(40)
    print(taxi)
    print("Fare ={:.2f}".format(taxi.get_fare()))
    taxi.start_fare()
    taxi.drive(100)
    print()
    print(taxi)
    print("Fare ={:.2f}".format(taxi.get_fare()))


main()
