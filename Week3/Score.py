import random
def Score_Calculation(score):
  if score < 0:
      return("{0} is Invalid score".format(score))
  else:
      if score > 100:
        return("{0} is Invalid score".format(score))
      if score > 50:
        return("{0} is Passable".format(score))
      if score > 90:
        return("{0} is Excellent".format(score))
      if score < 50:
        return("{0} is Bad".format(score))

def main():
    score = float(input("Enter score: "))
    File=open('results.txt','w')
    print(Score_Calculation(score),file=File)
    Therandom=random.randint(1,100)
    Score_Calculation(Therandom)
    print(Score_Calculation(Therandom), file=File)
    File.close()

main()