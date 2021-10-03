clock = False # Check if the clock must be made or not
period = "AM" # Variable to see which period it is

# Print all the hours of the day (am / pm)
while not clock:

    # Loop the hours from 1 to 12
    for hour in range(1, 13):
        hour_string = str(hour) # Make a string of the hour 

        time = hour_string + ":00" # Add the minutes after the hour

        # If the hour is "12", the periods get turned around to begin with the other period, else the standard period gets printed behind the hour
        if hour == 12:   
            time += "PM" if period == "AM" else "AM"

        else:
            time += "AM" if period == "AM" else "PM"

        print(time) # Print the hour to the terminal

    # If the loop is done
    else: 
        if period == "AM":
            period = "PM" # Change the time to "PM", if the hours for "AM" are printed
        
        else:
            clock = True # End the making of the clock