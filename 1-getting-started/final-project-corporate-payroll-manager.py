# defining the lists that will be used
names = []
hours_worked = []
hourly_rates = []

# function to calculate gross salary
def calculate_gross_pay(hours, rate) :
    if hours > 40 :
        gross_pay = (40 * rate) + ((hours - 40) * rate * 1.5)
        return gross_pay
    else :
        gross_pay = hours * rate
        return gross_pay
    
# function to calculate the tax rate on gross salary
def calculate_taxes(gross_pay):
    if gross_pay <= 1000 :
        net_pay = gross_pay
    elif gross_pay > 1000 and gross_pay <= 2000 :
        net_pay = gross_pay - (gross_pay * 0.10)
    else :
        net_pay = gross_pay - (gross_pay * 0.15)

    return net_pay

# loop for data input, validation, and error handling
while True :
    name = input("Please enter the employee's name (or 'done' to exit): ")

    if not name.replace(" ", "").isalpha() :
        print("Please, enter only letters.")
        continue

    if name.lower() == 'done' :
        print(f"\nInput session finish.\n")
        break

    try :
        hours = float(input("Please enter hours worked: "))
        if hours < 0 :
            print("Please enter a positive number.")
            continue

        rate = float(input("Please enter hourly pay rate: "))
        if rate < 0 :
           print("Please enter a positive number.")
           continue
            
    except :
        print("Please enter only numbers.")
        continue

    # stores input data (name, hours, rate) from the while loop
    names.append(name)
    hours_worked.append(hours)
    hourly_rates.append(rate)

# checking each stored item
print(f"{names} - \n{hours_worked}(hours) - \n{hourly_rates} (rate/hour)\n")

# use a 'for' loop to assign data to new variables, separating it by name
for i in range(len(names)) :

    current_name = names[i]
    current_hours = hours_worked[i]
    current_pay = hourly_rates[i]

    # call the functions responsible for storing each employee's gross and net salary
    current_gross = calculate_gross_pay(current_hours, current_pay)
    current_net = calculate_taxes(current_gross)

    # calculate how much was deducted in taxes
    tax_deducted = current_gross - current_net 

    # display all stored information once the user enters 'done'
    print(f"Employee {current_name}'s net salary is: US${current_net:.2f}\nTaxes deducted: US${tax_deducted:.2f} (Gross salary: US${current_gross:.2f})\n")

# display farewell message
print("\n--- Thank you for using the program. Come back anytime! ---\n")