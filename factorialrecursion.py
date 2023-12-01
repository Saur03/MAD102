def factorial_caculator(number):
    if number == 1:
        return 1
    else:
        return number * factorial_caculator(number - 1)
    

print('Welcome to our factorial calculator')
print('-'*55)

again = 'y'

while again == 'y':
    number = int(input('Please enter a number for our calculations: '))

    result = factorial_caculator(number)

    print(f'The factorial of {number} is {result}.')

    again = input('would you like to enter another number? y/n: ').strip().lower()

print('Thank you for using our calculator')
