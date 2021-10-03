total = 50 # Start with 50
cal_total = 50 # Make the same amount as the total, so that it can calculate the cal_total + 1 with the total

# Print all the number if the total is lower than 1000
while total <= 1000:
    
    print(total) # Print the total

    cal_total += 1 # Add 1 to the cal_total

    total += cal_total # Add the cal_total to the total