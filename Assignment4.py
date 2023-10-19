'''
Question1:- Create a function that when called, will display your full name and age to the screen.  
Make sure that it is proper sentence form.  For example, "Hello there - my name is Ben Kenobi and I am 78 years old."
Just build the function - no commenting required.

# Program Name: Creating a function
# Purpose: To call my full name and my age
# Author: Saurabh Chawla
# Date completed: 14 October, 2023

def name_age():
    myName = 'Saurabh Chawla'
    myAge = 26
    print(f'Hello there - my name is {myName} and I am {myAge} years old.')

# Call the function to display your name and age
name_age()

# Thank the user
print('Thank you for using the program')
'''
'''
Question2:- There are three (3) functions that you need to create for this question.
    #Function 1:
    #Create a function called highToLow.  It will take two numerical values as arguments.  
    #It will compare the two numebrs and it will return the highest and lowest. (5 marks)

# Program Name: Creating a function highToLow
# Purpose: To calculate highest and lowest
# Author: Saurabh Chawla
# Date completed: 14 October, 2023

def highToLow(num1, num2):
    if num1 > num2:
        highest = num1
        lowest = num2
    else:
        highest = num2
        lowest = num1
    return highest, lowest 

num1 = 10
num2 = 20
highest, lowest = highToLow(num1, num2)
print(f'The highest number is: {highest} and the lowest number is: {lowest}')

# Thank the user
print('Thank you using our program')

    #Function 2:
    #Create a function that takes in two numerical values.   
    #It will then take and multiply those two numbers together and return the product of both numbers. (5 marks)

# Program Name: Multiplication
# Purpose: To calculate the product of two number
# Author: Saurabh Chawla
# Date completed: 14 October, 2023

def multiplyNumbers(num1, num2):
    return num1*num2

num1 = int(input('Enter the first numbers: '))
num2 = int(input('Enter the second number: '))
result = multiplyNumbers(num1, num2)
print(f'The multiplication of {num1} and {num2} is: {result}')

# Thank the user
print('Thank you for using our program')


    #Function 3:
    #Create a function that tasks in two numerical values.  
    #It will then use the highToLow function to determine which is the lowest and highest numbers.  
    #It will then take and divide the highest by the lowest and return the result.
    #Just create the functions - no need to comment all your code.

# Program Name: creating a function and doing division of number using another function
# Purpose: firstly calculate lowest and highest number and then proceed the division and return the result
# Author: Saurabh Chawla
# Date completed: 14 October, 2023

def divideHighestByLowest(num1, num2):
    high, low = highToLow(num1, num2)
    if low == 0:
        return "Not possible (lowest number is zero)"
    return high/low

num1 = int(input('Enter the first numbers: '))
num2 = int(input('Enter the second number: '))
res = divideHighestByLowest(num1, num2)
print(f'The division of the highest by the lowest is: {res}.')
'''

'''
Question3:- 
This final question will require that you create an algorithm 
that will ask the user if they want to perform some mathematical calculations (Y), exit the program (N) or see your information (I)  
If they say Yes (enter Y), you will ask them to enter two numbers.  
You will then take those two numbers and using them, call your functions from question 2.  
Once completed, you will ask them if they want to repeat the process.
If they say No (enter N), thank them for using the program and exit.  
If they say Information (I), then you will call the function you made in question 1.
This program requires full commenting and ensure you follow the best practices detailed in class.
'''

# Program Name: creating an algorithm and perform some mathematical calculations
# Purpose: Ask the user to perform various calculations
# Author: Saurabh Chawla
# Date completed: 14 October, 2023

def name_age():
    myName = 'Saurabh Chawla'
    myAge = 26
    print(f'Hello there - my name is {myName} and I am {myAge} years old. ')

def multiplyNumbers(num1, num2):
    return num1*num2
  
def highToLow(num1, num2):
    if num1 > num2:
        highest = num1
        lowest = num2
    else:
        highest = num2
        lowest = num1
    return highest, lowest 

def divideHighestByLowest(num1, num2):
    high, low = highToLow(num1, num2)
    if low == 0:
        return "Not possible (lowest number is zero)"
    return high/low

while True:
    someOperations = input('Enter Y for mathematical operations or N to exit the program, otherwise I to see your information: ')
    if someOperations == 'Y':
        while True:
            num1 = int(input('Enter the first number: '))
            num2 = int(input('Enter the second number: '))

            print(f'The multiplication of both the numbers is {multiplyNumbers(num1, num2)}')

            print(f'The highest and lowest numbers are {highToLow(num1, num2)} respectively.')

            print(f'The result of dividing the highest number by the lowest is: {divideHighestByLowest(num1, num2)}')
            
            repeat = input('Do you want to repeat this process(Y/N)?')
            if repeat == 'N':
                print('Thank you for using our program.')
                break

    elif someOperations == 'N':
        print('Thank you for using our program and Exit. ')
        break

    else:
        name_age()