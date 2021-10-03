# name of student: Xander Briem
# number of student: 99061142
# purpose of program: Print a answer to the user how he can pay the total price with the fastest method
# function of program: Calculate how the user can pay the price 
# structure of program: loop through the program if the user has not paid the total price


receipt = [] # Array for the receipt

# Ask how many the user already paid, and change it into a number

paid = input("How many have you paid: ") 
paid = int( float(paid) * 100 )

# Ask how much the total price is, and change it into a number

toPay = input("Total price: ") 
toPay = int( float(toPay) * 100 ) 

change = toPay - paid # Calculate the change the user must pay


if change > 0: # Check if the user must pay more
    coinValue = 500 # The amount of cents the user must pay


# Ask the user questions if the user have not paid everything

while change > 0 and coinValue > 0: 
    nrCoins = change // coinValue # Calculate how many coins the user must give back with the coinValue amount
    
    # Change the coin value to "euro" or "cents"
    
    if coinValue >= 100:
        coinValue_name = " euro" 
        coinValue_str = str( coinValue // 100 ) # Change the value of the coin the user must pay, to a string

    else: 
        coinValue_name = " cents"
        coinValue_str = str(coinValue) # Change the value of the coin the user must pay, to a string


    if nrCoins > 0: # If the user can pay with a coin that is in the coin list

        nrCoins_str = str(nrCoins) # Number of coins the user must pay

        print("return maximal " + nrCoins_str + " coin(s) of " + coinValue_str + coinValue_name ) # Print the amount of coins the user must give back with the specific value

        nrCoinsReturned = input("How many coin(s) of " + coinValue_str + coinValue_name + " did you return? ") # Ask the user how many coins he has paid with the specific value
        nrCoinsReturned_int = int(nrCoinsReturned) # Change the input what the user has paid with the specific value to a number

        change -= ( nrCoinsReturned_int * coinValue ) # The change gets decreased with the value the user has paid\

        # If the coins the user has given back is higher than 0
        if nrCoinsReturned_int:

            # Add the information to the receipt array
            receipt_info = nrCoinsReturned + " coin(s) of " + coinValue_str + coinValue_name + " given back" 
            receipt.append(receipt_info) 



    coinArray = [500, 300, 200, 100, 50, 20, 10, 5, 2, 1, 0] # Array with all the coin values

    coinValue_position = ( coinArray.index(coinValue) + 1 ) # Get the position of the coin the user did answer + 1
        
    coinValue = coinArray[coinValue_position] # Change the coin value with the coinValue_position variable


# Print the answer if the user must pay more, or that the payment is completed

else:
    change_str = str(change) # Change the change the user must pay, to a string

    # If the user has not paid everything
    if change:
        print("Change not returned: " + change_str + " cent(s)") 
        
    # If the user paid everything
    else:  

        # Print every coin with the amount the user has given back
        for info in receipt:
            print(info)