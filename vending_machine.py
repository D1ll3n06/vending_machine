#Header
print()
print('***Welcome to All Stars Vending Machine***')

#Assign prices to each product
gum = 0.65
soda = 1.25
chips = 1.75
sandwich = 2.85

#Initialize the variables "total" and "item" as 0
total = 0
item = 0

#Loop until the total matches the price of an item
while(total != gum and total != soda and total != chips and total != sandwich):
    #Display menu
    print()
    print('Exact amount is required for purchase and to exit the vending machine system.')
    print()
    print('Select your purchase:')
    print('Chewing gum is $0.65')
    print('Soda beverage is $1.25')
    print('A bag of chips is $1.75')
    print('Price of a sandwich is $2.85')
    print('--------------------------------------')
    #Initialize variables "nickels", "dimes", "quarters", and "dollars" by converting a user input on the amount of each coin into their values in dollars
    nickels = float(input("Enter an amount of nickels: ")) * 0.05
    dimes = float(input("Enter an amount of dimes: ")) * 0.1
    quarters = float(input("Enter an amount of quarters: ")) * 0.25
    dollars = float(input("Enter an amount of dollars: "))
    
    #Add the values of each coin and dollar into a total
    total = nickels + dimes + quarters + dollars
    
    #Print a message only if the total doesn't match the price of any of the items that says "The amount you entered does not match any of the items"
    if(total != gum and total != soda and total != chips and total != sandwich):
        print()
        print('-----------------------------------')
        print("The amount you entered does not match any of the items.")
        print('Try entering another amount.')
        print()
        print()

#Set the item variable to a string based on which price the total matches with
if(total == gum):
    item = "pack of gum"
elif(total == soda):
    item = "soda"
elif(total == chips):
    item = "bag of chips"
elif(total == sandwich):
    item = "sandwich"

#Print a "Thank you" message corresponding to the item purchased
print()
print('-----------------------------------')
print(f'Cost of the {item} is ${total:,.2f}')
print("Thank you for purchasing a " + item +'!')
print()