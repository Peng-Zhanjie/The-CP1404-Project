
from programming_language import ProgrammingLanguage
langurage=[]
def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    langurage.append(ruby)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    langurage.append(python)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    langurage.append(visual_basic)
    print(ruby)
    print(python)
    print()
    print("The dynamically typed languages are:")
    for i in langurage:
        if(i.is_dynamic()==True):print(i.name)


main()