import random
Example=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,37,38,39,40,41,42,43,44,45]
def Quick_picks():
    Thesample=Example.copy()
    Times=int(input("How many quick picks?"))
    for h in range(Times):
      for i in range(6):
          x=random.choice(Thesample)
          for j in range(45):
              if(Thesample[j]==x):
                  del Thesample[j]
                  break
          print("{}".format(x),end=' ')
      print()


def main():
    Quick_picks()
main()