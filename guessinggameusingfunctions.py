#
#
#
#
import random
# Declare comparison function
def compare_numbers(guess, winning_number):
    if guess == winning_number:
        # they win!
        return True
    else:
        if guess>winning_number:
            print(f'Your guess of {guess} is too high')
        
        else:
            print(f'Your guess of {guess} is too low')
        # they lost... this round
        return False

# Declare variables
guess_count = 1
winning_number = random.randint(1,10)
print("*"*30)
print(winning_number)
print("*"*30)

# Introduce our program
print("Welcome to our guessing game!")
#ask for input until the guess the correct number or run out of tries
while guess_count < 4:
    guess = int(input(f'Please enter a number between 1 and 10 for guess #{guess_count}:'))

    result = compare_numbers(guess, winning_number)

    if result:
        print(f'Congratulations! You guessed the winning number {winning_number}')
        guess_count = 4
        #break
    else:
        guess_count += 1


print(f'The winning number was {winning_number}')
# thank the user
print('Thank you for using our program')
