entry = input("Enter the value you want to withdraw: US$")

try :
    withdraw = int(entry)
except :
    print("Error, Please Enter a Number")
    quit()

min_amount = 10
max_amount = 500

if withdraw < min_amount :
    print(f"Error, Minimum Withdrawal Amount is US${min_amount}")
elif withdraw > max_amount :
    print(f"Error, Maximum Withdrawal Amount is US${max_amount}")
elif withdraw % 10  != 0 :
    print("Error, Withdrawal Amount must be a Multiple of US$10")
else :
    print(f"Withdrawal Approved, Please Take Your Cash US${withdraw}")