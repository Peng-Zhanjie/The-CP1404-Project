"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    NumberOfmonths = int(input("How many months? "))

    for month in range(1, NumberOfmonths+1):
        income = float(input("Enter income for month {}".format(month) + ": "))
        incomes.append(income)

    ListIncome=list(enumerate(incomes, start=1))

    print("\nIncome Report\n-------------")
    total = 0
    for month in ListIncome:
        income = month[1]
        total += income
        print("Month {:2} - Income:${:10.2f} Total:${:10.2f}".format(month[0],income,total))


main()