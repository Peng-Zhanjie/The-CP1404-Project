import random
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
MIN_LENGTH = 2
MAX_LENGTH = 8
SPECIAL_CHARS_REQUIRED = False

def  is_valid_format(word_format):
    Length=len(word_format)
    Isvalid=True
    for i in range(Length):
        if(word_format[i]!="c")and(word_format[i]!="v"):Isvalid=False
    if (Isvalid==True):return True
    else:return False

def Input_Wordformat():
  Reloop=True
  while(Reloop==True):
    word_format = input("Please enter your words with 'c','v':")
    word_format=word_format.lower()
    word = ""
    if(is_valid_format(word_format)==True):
      Reloop=False
      for kind in word_format:
          if kind == "c":
              word += random.choice(CONSONANTS)
          elif kind =="v":
              word += random.choice(VOWELS)
          elif kind.isalpha()==True:
              word += kind
    else:
        print("Invalid word format:")

  print(word)



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