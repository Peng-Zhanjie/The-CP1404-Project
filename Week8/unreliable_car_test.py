from unreliable_car import UnreliableCar


def main():
    taxi = UnreliableCar("Prius 1", 100, 50)
    taxi.drive(20)
    print(format(taxi) + "\n")
    taxi.drive(20)
    print(format(taxi) + "\n")
    taxi.drive(20)
    print(format(taxi) + "\n")
    taxi.drive(20)
    print(format(taxi) + "\n")
    taxi.drive(20)
    print(format(taxi) + "\n")


main()
