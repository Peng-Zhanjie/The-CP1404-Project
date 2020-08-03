def main():
    print("Electricity bill estimator ")
    cent=float(input("Enter cents per kWh:"))
    DailyUse=float(input("Enter daily use in kWh:"))
    Days=int(input("Enter number of billing days:"))
    bill=cent*DailyUse*Days/100
    print("Estimated bill: ${:.2f}".format(bill))
    TARIFF_11 = 0.244618
    TARIFF_31 = 0.136928
    print("Electricity bill estimator 2.0 ")
    reload=1
    while reload==1:
        TARIFF=int(input("Which tariff? 11 or 31:"))
        if TARIFF!=11 and TARIFF!=31: print("invalid input")
        else :reload=0
    DailyUse=float(input("Enter daily use in kWh:"))
    Days=int(input("Enter number of billing days:"))
    if TARIFF==11: bill=DailyUse*Days*TARIFF_11
    elif TARIFF==31: bill=DailyUse*Days*TARIFF_31
    print("Estimated bill: ${:.2f}".format(bill))
main()