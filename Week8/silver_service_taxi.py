from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5
    price_per_km = 1.23

    def __init__(self, name="",fuel=100,  fanciness=1):
        self.name = name
        self.fuel = fuel
        super().__init__(name,fuel)
        self.price = self.price_per_km * fanciness

    def get_fare(self):
        fare = super(SilverServiceTaxi, self).get_fare() + self.flagfall
        return fare

    def __str__(self):
        return "{}, fuel={}, odo={}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(self.name, self.fuel,
                                                                                               self.odometer,
                                                                                               self.current_fare_distance,
                                                                                               self.price,
                                                                                               self.flagfall)
