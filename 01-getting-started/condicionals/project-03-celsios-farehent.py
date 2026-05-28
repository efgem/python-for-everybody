temp = input("Enter Celsius Temperature: ")

try :
    cel = float(temp)
except :
    print("Error, Please Enter a Number")
    quit()

fah = (cel * 1.8) + 32

if fah >= 100 :
    print("Alert, High Temperature: F°", fah)
else :
    print("Temperature in F°: ", fah)