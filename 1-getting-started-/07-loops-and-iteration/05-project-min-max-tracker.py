largest = None
smallest = None

while True :
    entry = input("Please Enter an int number: ")

    if entry.lower() == "done": # if the user enters 'done', the program will stop and display the results
        print("\nSession finished.\n")
        break #

    try : ## this is the part that checks if the user actually entered a number
        num = int(entry) 

    except : 
        print(f"Invalid input.\nTry again\n")
        continue ##

    if largest is None or num > largest : ### will assign the largest number entered to the 'largest' variable
        largest = num ###

    if smallest is None or num < smallest : #### will assign the smallest number entered to the 'smallest' variable
        smallest = num ####

print(f"Maximum is: {largest}")
print(f"Minimum is: {smallest}\n")