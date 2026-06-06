# Work in progress

names = []
grades = []

while True :
    name = input("Enter your name ( or done to finish ): ")
    if name.lower() == "done" :
        print("Please enter letters.")
        break

    entry = (input(f"Hello, {name} enter your grade: "))
    
    try :  
        grade = float(entry)

    except : 
        print("Please, enter a float/int number.")
        continue

    if grade < 0  or grade > 100 :
        print("Please enter a grade between 0 and 100.")
        break        
    

    names.append(name)
    grades.append(grade)