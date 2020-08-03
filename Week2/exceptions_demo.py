IFnore=True
while IFnore==True:
 try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator==0 : print("You've jump the ZeroDivisionError, but denominator must be a valid number.")
    else:
        fraction = numerator / denominator
        print("{:.3f}".format(fraction))
        IFnore=False
 except ValueError:
    print("Numerator and denominator must be valid numbers!")
 except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur?

# If you put alphabet in it.

# When will a ZeroDivisionError occur?

# If you put zero as denominator.

# Could you change the code to avoid the possibility of a ZeroDivisionError?

# The modification has been completed in the file.
