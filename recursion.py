'''
Question1:- Create a function that is called - to the power of.  It will take in two values - a base number and an exponent.  The function will do the following:

If the exponent value is 0 - then return 0 from the function
If the exponent value is 1 - then return the base number
Otherwise, the function will call your function recursively
You will build an algorithm that will ask the user for a base number and an exponent.  

If either of the values the user enters is not a number, display an error message.  

Use exception handling for this - you should keep asking until you get numerical values.  
If the numerical values are correct, it will run your recursive function and display results like this:

Here are some examples of your output:

If the base number is 2 and the exponent is 0 we will get this result displayed in the console:

The result of 2 to the exponent 0 is equal to 0

If the base number is 2 and the exponent is 1 we will get this result displayed in the console:

The result of 2 to the exponent 1 is equal to 2

If the base number is and the exponent is 4 we will get this result displayed in the console:

The result of 2 to the exponent 4 is equal to 16
'''

# Program- Recursive Program
# Purpose- To built a power of program using recursive function and exception handling
# Name- Saurabh Chawla
# Date - 1 December 2023

# making a function
def powerOf(baseNumber, exponent):
    if exponent == 0:
        return 0
    elif exponent == 1:
        return baseNumber
    # Create a recursive and call it
    else: 
        return baseNumber * powerOf(baseNumber, exponent - 1)

# Introduction    
print('Welcome to our baseNumber and exponent program')
print('-'*55)

# main program and use exception handling
while True:
    try:
        baseNumber = int(input('Please enter a base number: '))
        exponent = int(input('Please enter the exponent number: '))

        result = powerOf(baseNumber, exponent)
        print(f'The result of {baseNumber} to the exponent {exponent} is equal to {result}. ')
        break
    except:
        print('Invalid number! Please enter numeric Values.')

    
# Thank the user
print('Thank you for using our program. ')    
