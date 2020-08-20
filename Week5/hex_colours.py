Colour={"AliceBlue":"#f0f8ff","AntiqueWhite":"#faebd7","azure":"#f0ffff","blue":"#0000ff","brown":"#a52a2a","coral":"#ff7f50","DeepSkyBlue":"#00bfff",
        "gold":"#ffd700","gray":"#bebebe","GreenYellow":"#adff2f","PaleGreen":"#98fb98","pink":"#ffc0cb","white":"#ffffff"}

def colours():
     loop=True
     print(Colour)
     while loop==True:
             Enter=input("Enter a name of color:")
             if(Enter==""):
                     print("Finished")
                     loop=False
             elif Enter.isalpha()==False:print("Invalid Input, please enter a word")
             else:
                     if Enter in Colour.keys():
                             print(Colour[Enter])
                     else:print("Can not find in Dictionary")


colours()