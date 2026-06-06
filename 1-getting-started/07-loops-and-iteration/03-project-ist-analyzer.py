count = 0
sum = 0
greater66 = []

for i in [22, 33, 44, 55, 66, 77, 88] :

    if i > 66 : # verification of numbers greater than 66
        greater66.append(i)

    count = count + 1 # count
    sum = sum + i # sum of the numbers in the list

    print(f"{count} - {sum} - {i}")

numbers_cleaner66 = ", ".join(str(n) for n in greater66) # convert numbers to strings and join them with commas

print(f"\nThe numbers greater than 66 are: {numbers_cleaner66}")
print(f"\nYour list has: {count} numbers\nThe sum of your list is: {sum}\n")