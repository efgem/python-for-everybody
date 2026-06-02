distance = input("Please Enter The Delivery Distance In Kilometers: ")

try :
    distance_input = float(distance)
except :
    print("Enter a Number.")
    quit()

def calculate_delivery(km) :
    if km <= 5 :
        totalpay = 5
        return totalpay
    elif km > 5 :
        totalpay = 5 + ((km - 5) * 1.5)
        return totalpay

final_pay = calculate_delivery(distance_input)

print(f"Total Pay: US${final_pay}")