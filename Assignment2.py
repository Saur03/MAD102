'''
Question 1:

# Program Name: Good standings program
# Purpose: To find the status of the student
# Author: Saurabh Chawla
# Date completed: 25th September, 2023

# Declare variable
gpa = 0.0

# Program Introduction
print('Welcome to the good standings program')

# Get the variable values
allPass = input('Enter Y if you have passed all your courses otherwise N: ')
gpa = float(input('Enter your gpa: '))

# Calculate status
if allPass == "Y" and gpa > 2.0:
    status = "good standing"
else:
    status = "dismissal 1"

# Output results
print(f'Are all courses passed: {allPass}')
print(f'Your scored total gpa is {gpa:.2f}')
print(f'Your overall status is {status}')

# Thank the user
print('Thank you for using our program.')


Question 2:
For all dinners, our restuarant automatically adds a 10% tip to all orders.  
For example, a $10.00 meal actually costs $11.00 with the tip. 
Create a program that wil ask the user for the amount of money they have and the total cost of the food they want to order. 
Our program will calculate the appropriate tip and add it to the total and determine whether they have enough money to purchase the food. 
If they do, it will display that they have enough money and also display the change returned. 
If they do not, it will display how much more money they in order to make the purchase.


# Program Name: Dinners restaurant
# Purpose: To calculate total cost including tip and decide if moeny is sufficient
# Author: Saurabh Chawla
# Date completed: 25th September, 2023

# Declare variable
tip = 0.1 #10/100

# Program Introduction
print('Welcome to the dinners program')

# Get the variable values
moneyHave = float(input('Enter the amount of money you have: $'))
orderCost = float(input('Enter the total cost of the food you want to order: $'))

# Calculate tip and update order cost
totalTip = orderCost * tip
orderCost += totalTip
change = moneyHave-orderCost

# Output results
if moneyHave >= orderCost:
    print(f'You have enough money to order and your change is: ${change:.2f}')
else:
    change *= -1
    print(f'You do not have enough money. You need ${change:.2f} more')

# Thank the user
print('Thank you for using our program.')


Question 3:
'''
# Program Name: We Ship Anything
# Purpose: To calculate the charges associated with the weight of a specific package
# Author: Saurabh Chawla
# Date completed: 25th September, 2023

# Declare variable
baseRate = 12.50

# Program Introduction
print('Welcome to We Ship Anything')

# Get the variable values
name = input('Enter your name: ')
cityShipped = input('Enter the city where you want to ship package: ')
packageWeight = float(input('Enter the weight of the package: '))

# Calculate the additional charge
if packageWeight <= 3.0:
    premiumAmount = 4.25
elif packageWeight > 3.0 and packageWeight <= 5.0:
    premiumAmount = 6.50
else:
    premiumAmount = 12.99

if cityShipped != "Ottawa":
    handlingCharge = 8.55
else:
    handlingCharge = 0

totalCost = baseRate + premiumAmount + handlingCharge

# Output results
print(f'Customer name: {name}')
print(f'City shipping to: {cityShipped}')
print(f'Base rate: ${baseRate:.2f}')
print(f'Premium amount: ${premiumAmount:.2f}')
print(f'Handling charge: ${handlingCharge:.2f}')
print(f'Total charge: ${totalCost:.2f}')

# Thank the user
print('Thank you for using our program.')