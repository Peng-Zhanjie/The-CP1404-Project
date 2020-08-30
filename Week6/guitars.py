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
    my_guitar=[]
    my_guitar.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    my_guitar.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("My guitars!")
    loop=True
    while loop==True:
      name=input("Name:")
      if(name==""):
          print("Input finished.\n")
          loop=False
          break
      loop1=True
      while loop1==True:
          try:
              year=int(input("Year:"))
              loop1=False
          except ValueError:print("Invalid input")
      loop2=True
      while loop2==True:
          try:
              cost=float(input("Cost:"))
              cost=float("%.2f" % cost)
              loop2=False
          except ValueError:print("Invalid input")
      my_guitar.append(Guitar(name,year,cost))
      print()


    count=0
    for guitar in my_guitar:
        count+=1
        print("Guitar {}: {} ({}), worth ${}".format(count,guitar.name,guitar.year,guitar.cost))




main()