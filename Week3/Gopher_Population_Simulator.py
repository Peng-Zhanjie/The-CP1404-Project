import random
def main():
    Population=1000.00
    print("Welcome to the Gopher Population Simulator!")
    print("Starting population: {}".format(Population))
    for i in range(10):
        Born=random.uniform(0.1,0.2)
        Death=random.uniform(-0.05,-0.25)
        print("Year {}".format(i))
        print("{0} gophers were born. {1} died.".format(int(Population*Born),int(Population*Death)))
        Population = int(Population * (1 + Born + Death))
        print("Population:{}".format(Population))

main()