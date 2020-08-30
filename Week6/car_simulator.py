from car import Car
def Menu(my_car):

    loop=True
    while loop==True:
      print("{},fuel={},odo={}".format(my_car.name,my_car.fuel,my_car.odometer))
      print("Menu:")
      print("d) drive")
      print("r) refuel")
      print("q) quit")
      choice=input("Enter your choice:")
      if choice=="d":
          loop1=True
          while loop1==True:
            try:
                length=int(input("How many km do you wish to drive?"))
                if length<=0: print("Distance must be >= 0")
                else:
                    distance=my_car.drive(length)
                    loop1=False
                    print("The car drove {}km.".format(distance))
            except ValueError:
                print("Invalid input")
      elif choice=="r":
          loop2=True
          while loop2==True:
            try:
                fuel=int(input("How many units of fuel do you want to add to the car?"))
                if fuel<=0: print("Distance must be >= 0")
                else:
                    print("Added {} units of fuel.".format(fuel))
                    my_car.add_fuel(fuel)
                    loop2=False
            except ValueError:
                print("Invalid input")

      elif choice=="q":
          print("Good bye {}'s driver.".format(my_car.name))
          loop=False
      else:
          print("Invalid choice")


def main():
    print("Let's drive!")
    name=input("Enter your car name:")
    my_car=Car(100,name)
    Menu(my_car)


main()