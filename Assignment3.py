'''
Question1: We are running a phone answering business that charges for each phone call we receive.  
We have three clients that are represented by the following codes - 
Frank's Hot Chocolate (F), Tobias's Waffles (W) and Peter's Cotton Candy (P).  
We want to create a program that we can use througout the day.  
As we answer a call, we will enter the code for the specific client.  
We will continue to use this program until the end of the day has been reached.  
We will then enter E to exit the program and the program will print out a display of the total (sum) for each client.  
It could be that we have a slow day and have no calls for certain clients, or all clients, we still need to display that.  
Create this program.  Assume that the user is entering the correct letter - a capitalized version of the code.
'''

# Program Name: Phone answering business program
# Purpose: The user is entering the correct letter and the total for each client.
# Author: Saurabh Chawla
# Date completed: 2nd October, 2023

# Declare variables
FranksHotChocolate = 0
TobiasWaffles = 0
PetersCottonCandy = 0

# Program Introduction
print('Welcome to phone answering business program')

# Calculate
while True:
    clientCode = input('Enter client codes(F,W,P) or E to exit: ')
    if clientCode == 'E':
        break;
    elif clientCode == 'F':
        FranksHotChocolate += 1
    elif clientCode =='W':
        TobiasWaffles += 1
    elif clientCode == 'P':
        PetersCottonCandy += 1
    else:
        print('Invalid Code, please enter \'F\' or \'W\' or \'P\' or \'E\'')

# Output Results
print(f'Total calls for Frank\'s Hot Chocolate (F): {FranksHotChocolate}')
print(f'Total calls for Tobias\'s Waffles (W): {TobiasWaffles}')
print(f'Total calls for Peter\'s Cotton Candy (P): {PetersCottonCandy}')



'''
Question2: Create a program that will ask the user for an ending number.  
It will display all the numbers from 0 to that ending number - except for numbers that are evenly divisible by 4.  
For example, if the ending number was 11, it would display 0 1 2 3 5 6 7 9 10 11.
'''

# Program Name: Displaying the non divisible numbers
# Purpose: displaying the numbers from 0 till ending number and except for that numbers which are evenly divisible by 4
# Author: Saurabh Chawla
# Date completed: 2nd October, 2023

# Program Introduction
print('Welcome to displaying numbers not divisible by 4')

# get the variables displayed
endingNumber = int(input('Enter the ending number: '))

# Calculate and print output
for i in range(0, endingNumber + 1):
    if (i % 4 != 0) or (i == 0):
        print(i)


'''
Question 3:- We are creating a special character printing program.  
Ask the user for a special character and then ask them the number of times they want it displayed.  
Display the special character the specified number of times to the screen.  Do so in a single row.
'''
# Program Name: Special character printing program
# Purpose: displaying the special character for the specified number of times
# Author: Saurabh Chawla
# Date completed: 2nd October, 2023

# Declare variables
i = 0

# Program Introduction
print('Welcome to special character printing program')

# get the variables displayed
specialCharacter = input('Enter the special character: ')
numberOfTimes = int(input('How many times do you want to displayed it: '))

# displaying the special character for the specified number of times to the screen
print(f'The number of special character on the screen will be: {numberOfTimes}' )
for i in range(numberOfTimes):
    # display output
    print(f'{specialCharacter} ', end="")
'''
'''