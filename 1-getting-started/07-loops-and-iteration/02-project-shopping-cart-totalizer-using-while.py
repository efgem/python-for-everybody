total = 0 

while True :
    try : # Check if it really is a number
        entry = input("Please Enter The Total Value Of The Items In Your Shopping List: US")
        items = float(entry)

        if items == 0 : # System to pause when the customer types "0"
            break

        total += items # Logic to sum the items that are entered
        print(f"Subtotal is: US{total:.2f}\n")
            
    except : # If it's not a number, then:
        print(f"Error, Please Enter Numbers. \n") 
        continue # If the user enters a letter, the "try" block fails and the "except" block is triggered. The "continue" statement ensures that Python ignores the rest of the loop and goes straight back to the ""input" line to request the data again

print(f"The Total Amount To Be Paid In The Shopping Cart Is: US{total:.2f}")