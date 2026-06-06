largest_so_far = -1

print("The number before the loop was:", largest_so_far)

for num in[3,2,5,21,33,2,223,32,444] :
    if largest_so_far < num :
        largest_so_far = num
    print(largest_so_far, num)

print("The number after the loop is:", largest_so_far)