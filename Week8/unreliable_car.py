from car import Car
import random

class UnreliableCar(Car):
    def __init__(self,name="", fuel=0,reliability=0):
        super().__init__(name, fuel)
        self.reliability=reliability

    def drive(self,distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        random_number=random.randint(1,100)
        if random_number>self.reliability:
            print("Invalid drive, car stopped.")
        else:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
        return distance