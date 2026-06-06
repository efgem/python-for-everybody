entry = input("Please enter your age: ")

try :
    age = int(entry)
except :
    print("Error, Please Enter a Number")
    quit()

if age < 0 or age > 120 :
    print("Error, Please Enter a Valid Age")
elif age < 18 :
    print("Access Denied, You are too Young")
else :
    print("Access Granted, Welcome!")
