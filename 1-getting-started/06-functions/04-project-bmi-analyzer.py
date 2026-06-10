def analyze_bmi(weight, height) :
    
    bmi = weight / (height * height)

    if bmi < 18.5 :
        category = "Underweight"
    elif bmi < 24.9 :
        category = "Normal Weight"
    elif bmi < 29.9 :
        category = "Overweight"
    else :
        category = "Obesity"

    return bmi, category

try :

    user_weight = float(input("Enter your weight (KG): "))
    user_height = float(input("Enter your height (M): "))

    user_bmi, user_category = analyze_bmi(user_weight, user_height)

    print(f"\nYour BMI is: {user_bmi:.2f}")
    print(f"Category: {user_category}")

except :
    print("Error. Please enter numbers.")