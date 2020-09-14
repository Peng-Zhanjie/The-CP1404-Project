from car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23

    def __init__(self, name="",fuel=100, ):
        self.fuel = fuel
        self.name = name
        super().__init__( name,fuel)
        self.price = self.price_per_km
        self.current_fare_distance = 0

    def get_fare(self):
        fare = round(self.current_fare_distance * self.price, 1)
        return fare

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(int(distance))
        self.current_fare_distance += distance_driven
        return distance_driven

    def start_fare(self):
        self.current_fare_distance = 0

    def __str__(self):
        return super().__str__() + ",{}km on current fare, ${:.2f}/km".format(self.current_fare_distance,
                                                                              self.price_per_km)
