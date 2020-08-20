dictionary_of_email={}
loop=True
while loop==True:
    email=input("Email:")
    if email=="": loop=False
    elif "@" not in email:print("Invalid")
    else:
        loop1=True
        while loop1==True:
          record=email.split("@")
          ifname=input("Is your name {}? (Y/n)".format(record[0])).upper()
          if(ifname=="Y")or(ifname=="YES"):
              Name=record[0]
              loop1=False
          elif(ifname=="N")or(ifname=="NO"):
              loop1=False
              loop2=True
              while loop2!=False:
                  Name=input("Name:")
                  if (Name.isalpha()==False) or (Name==""):print("Invalid Name")
                  else: loop2=False
          else:print("Invalid input")
        dictionary_of_email[Name]=email

for emails in dictionary_of_email:
    print("{}".format(emails),"({})".format(dictionary_of_email[emails]))

