hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate/Hour: US$"))
vhours = 40
multiplier = 1.5

def computepay(hrs, rate):
    if hrs <= vhours :
        ratec = hrs * rate
        return ratec
    elif hrs > vhours :
        ratec = (vhours * rate) + ((hrs - vhours) * rate * multiplier)
        return ratec

print(f"Pay: US${computepay(hrs, rate)}")
