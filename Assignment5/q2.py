
# Program Name: even/odd game
# Purpose: To display the even and odd numbers and do some operations
# Author: Saurabh Chawla
# Date: 24 October 2023

# Program Introduction
print('Welcome to even/odd game')

playGame = input('Do you want to play the even/odd game (Y/N)? ').lower()
while True:
    if playGame.startswith("n"):
        print('We are sorry that you do not want to play')                                                         
        break
    
    elif playGame.startswith("y"):
        number = int(input('Enter an integer: '))
        evenOdd = input('Provide input to see the corresponding even or odd numbers up to that number: ').lower()
        if evenOdd.startswith('e'):
            print(f'even number upto {number}: ')
            for i in range(number + 1):
                if i % 2 == 0:
                    print(i)
        elif evenOdd.startswith('o'):
            print(f'Odd numbers up to {number}: ')
            for i in range(number + 1):
                if i % 2 != 0:
                    print(i)
        else:
            print('Invalid Choice. Please enter even or odd or the corresponding first character.' )

        playAgain = input('Do you want to play the game(Yes/No)? ').lower()
        if playAgain.startswith("y"):
            continue
        else:
            break
    else:
        print('Invalid Selection. Please enter again')
        continue 
    
# Thank the user
print('Thank you for using our program')