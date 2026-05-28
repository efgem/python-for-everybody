hrs = float(input("Enter Hours: "))
rate = float(input("Enter Hourly Rate: "))

if hrs <= 40:
    pay = hrs * rate
    print("Your Total Pay is: US$", pay)
else:
    pay = 40 * rate
    tpay = ((hrs - 40) * (rate * 1.5)) + pay 
    print("Your Total Pay with Overtime: US$", tpay)

    