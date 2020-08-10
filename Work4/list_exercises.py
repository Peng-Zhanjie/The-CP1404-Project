usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
def main():
    numbers=[]
    Count=0
    read=True
    while (read!=False):
        try:
            number=int(input("Please enter number{}:".format(Count+1)))
        except ValueError:
            print("ValueError")
            continue
        if(number>=0):
            numbers.append(number)
            Count+=1
        else:
            print("Input finished")
            read=False
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The biggest number is {}".format(max(numbers)))
    Average=sum(numbers)/len(numbers)
    print("The average of the numbers is {}".format(Average))

    loop=True
    while(loop==True):
        name=input("Please enter your name:")
        if name not in usernames:print("Access denied")
        else:
            print("Access granted")
            loop=False



main()