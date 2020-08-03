import random
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
UPPERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERS="abcdefghijklmnopqrstuvwxyz"
DIGITS="1234567890"
MIN_LENGTH = 2
MAX_LENGTH = 8
SPECIAL_CHARS_REQUIRED = False
def Input_Wordformat():
  word_format = input("Please enter your words with '#','%' or '*':")
  word = ""
  for kind in word_format:
      if kind == "#":
          word += random.choice(CONSONANTS)
      elif kind =="%" or kind=="*":
          word += random.choice(VOWELS)
      elif kind.isalpha()==True:
          word += kind
  print(word)

def Random_Wordformat():
    Jug=True
    while Jug!=False:
        try:
            count_length = int(input("Enter the length of wordformat:"))
            Jug=False
        except ValueError: print("ValueError")
    count_upper= input("Enter whether the upper words are needed(True or False):")
    count_lower = (input("Enter whether the lower words are needed(True or False):"))
    count_digit = (input("Enter whether the digits are needed(True or False):"))
    count_special =(input("Enter whether the special characters are needed(True or False):"))

    word=""
    choic=[]
    if (count_upper.upper()=="TRUE"): choic.append("U")
    if (count_lower.upper() == "TRUE"): choic.append("L")
    if (count_digit.upper() == "TRUE"): choic.append("D")
    if (count_special.upper()== "TRUE"): choic.append("S")

    for i in range(count_length):
        x=random.choice(choic)
        if x=="U": kind=random.choice(UPPERS)
        elif x=="L": kind=random.choice(LOWERS)
        elif x=="D": kind=random.choice(DIGITS)
        elif x== "S": kind=random.choice(SPECIAL_CHARACTERS)
        word += kind
    print("The word made by generator is",word)
    if not is_valid_password(word):
        print("Invalid password!")
    print("Your {}-character password is valid: {}".format(len(word),word))

def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    count_length=len(password)
    if (count_length<MIN_LENGTH) or (count_length>MAX_LENGTH): return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for i in range(count_length):
        # TODO: count each kind of character (use str methods like isdigit)
        if(password[i].islower()==True):count_lower+=1
        elif(password[i].isupper() == True):count_upper += 1
        elif(password[i].isdigit() == True): count_digit += 1
        elif(password[i] in SPECIAL_CHARACTERS):count_special += 1

    # TODO: if any of the 'normal' counts are zero, return False
    if  (count_digit==0) or (count_upper==0) or (count_lower==0) : return False
    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
    if(SPECIAL_CHARS_REQUIRED==True):
        if(count_special==0): return False
    # if we get here (without returning False), then the password must be valid
    return True



Input_Wordformat()
Random_Wordformat()