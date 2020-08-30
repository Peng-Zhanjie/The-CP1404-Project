"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT" : "Northern Territory", "WA" : "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)
NAME_TO_CAPITAL={"Queensland": "Brisbane","New South Wales":"Sydney","Northern Territory":"rwin","Western Australia":"Perth","Australian Capital Territory":"Canberra","Victoria": "Melbourne","Tasmania": "Hobart"}

state_code = input("Enter short state: ")
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")



print(NAME_TO_CAPITAL)
Capital_code = input("Enter the state name: ").title()
while Capital_code != "":
    if Capital_code in NAME_TO_CAPITAL:
        print( NAME_TO_CAPITAL[Capital_code],"is the capital of",Capital_code)
    else:
        print("Invalid short state")
    Capital_code = input("Enter the state name: ").title()


Dictionary=CODE_TO_NAME.keys()
for i in Dictionary:
    print(i,"is",CODE_TO_NAME[i])