def fibonacci(number):
    if number == 0 or number == 1:
        return number
    else:
        return fibonacci(number - 2) + fibonacci(number - 1)
    
print('Welcome to our fibonacci sequence program')

sequence_number = int(input('Please enter a number for the fibonacci sequence: '))

for index in  range(sequence_number):
    print(f'{fibonacci(index)}', end=', ')

print(fibonacci(sequence_number))