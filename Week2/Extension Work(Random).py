#random Boolean
import random
MAX_INCREASE=50
def randbool():
    #First one
    x=bool(random.randint(0,1))
    print("The first rand bool is {}".format(x))
    #second one
    y=bool(random.getrandbits(1))
    print("The second rand bool is {}".format(y))
    #Third one
    z=random.choice([True, False])
    print("The second rand bool is {}".format(z))
    MAX_INCREASE=random.uniform(1,100)
    print("MAX_INCREASE is {:.2f}".format(MAX_INCREASE))



randbool()

