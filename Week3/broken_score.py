import random
def Score_Calculation(score):
  if score < 0:
      print("{0} is Invalid score".format(score))
  else:
      if score > 100:
        print("{0} is Invalid score".format(score))
      if score > 50:
        print("{0} is Passable".format(score))
      if score > 90:
        print("{0} is Excellent".format(score))
      if score < 50:
        print("{0} is Bad".format(score))

def main():
    score = float(input("Enter score: "))
    Score_Calculation(score)
    Therandom=random.randint(1,100)
    print("The random program:")
    Score_Calculation(Therandom)

main()