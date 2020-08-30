
class Guitar:
    def __init__(self,name="", year=0, cost=0):
        self.name=name
        self.year=year
        self.cost=cost

    def __str__(self):
        return "{} ({}): ${}".format(self.name,self.year,self.cost)

    def get_age(self):
        return 2020-self.year

    def is_vintage(self):
        if(self.get_age()>=50):return True
        else:return False

def main():
    Gibson=Guitar("Gibson L-5 CES",1922,16035.40)
    Anotherguitar=Guitar("Anotherguitar",2013)
    print(Gibson)
    print("Gibson L-5 CES get_age() - Expected 98. Got {}".format(Gibson.get_age()))
    print("Another Guitar get_age() - Expected 7. Got {}".format(Anotherguitar.get_age()))
    print("Gibson L-5 CES is_vintage() - Expected True. Got {}".format(Gibson.is_vintage()))
    print(("Another Guitar is_vintage() - Expected False. Got {}".format(Anotherguitar.is_vintage())))

main()