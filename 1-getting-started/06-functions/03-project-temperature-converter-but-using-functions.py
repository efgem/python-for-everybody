def convert_temp(temp, scale) :

    if scale.upper() == "C":
        return (temp * 9/5) + 32
    elif scale.upper() == "F":
        return (temp - 32) * 5/9
    else:
        return None

try : 

    user_temp = float(input("Enter the temperature: "))
    user_scale = input("Enter the scale (C for Celsius to Fahrenheit / F for Fahrenheit to Celsius): ")

    result = convert_temp(user_temp, user_scale)

    if result == None :
        print("Please enter 'C' or 'F'.")
    else :
        if user_scale.upper() == "C" :
            print(f"Converted Temperature: {result:.2f}ºF")
        elif user_scale.upper() == "F" :
            print(f"Converted Temperature: {result:.2f}ºC")

except :
    print("Please enter a valid numeric temperature.")