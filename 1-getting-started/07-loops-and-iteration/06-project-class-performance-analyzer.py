# lists created to store the names and grades
names = []
grades = []

# loop to ask for names and grades
while True :
    name = input("Enter your name ( or done to finish ): ")

    if name.lower() == "done" :
        print("\nData entry finished.")
        break

    entry = (input(f"Hello, {name} enter your grade: "))
    
    # system to check if the grade is actually a number
    try :  
        grade = float(entry)
    except : 
        print("Please, enter a float/int number.")
        continue

    if grade < 0  or grade > 100 :
        print("Please enter a grade between 0 and 100.")
        continue

    # saving the names in the created lists    
    names.append(name)
    grades.append(grade)

print("\n--- CLASS REPORT ---\n")

# match names with grades
for i in range(len(names)) :
    act_names = names[i]
    act_grades = grades[i]

    # determine pass/fail status
    if act_grades >= 60 :
        status = "Approved"
    else :
        status = "Failed"

    # will display the name, grade, and pass/fail status
    print(f"{act_names} - {act_grades} - {status}")

# system that will read the number of students to add: total number of students, average grade, highest and lowest grade
if len(names) > 0 :

    total_students = len(names)
    class_average = sum(grades) / len(names)
    highest_grade = max(grades)
    lowest_grade = min(grades)

    print(f"\n--- CLASS STATISTICS ---\n")

    print(f"Total students: {total_students}")
    print(f"Class Average: {class_average}")
    print(f"Highest Grade: {highest_grade}")
    print(f"Lowest Grade: {lowest_grade}\n")

else :
    print("\nNo data entered.\n")