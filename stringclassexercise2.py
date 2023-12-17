# Program Name: Word verification program
# Purpose: Determine the longest word - will also detect if they are the same word or same length
# Author: Richard Grayson
# Date completed: September 2023

# Determine the longest word from two passed words
# Return a tuple that holds teh longest word first, shortest second
def longest_word(first_word, second_word):
    # check if the length of the first word is longer than the second
    if len(first_word) > len(second_word):
        return first_word, second_word
    else:
        return second_word, first_word 

# Determine if the words are the same length
# Return true if they are the same length, false if not
def same_length(first_word, second_word):
    # check if the length is the same for both words
    if len(first_word) == len(second_word):
        return True
    else:
        return False

# Determine if the words are the same word
# Return true if they are the same word, false if they are not
def same_word_check(first_word, second_word):
    # check if it is the same word - move them both to uppercase letters so they can be equally compared
    # could also have sent them both to lowercase letters
    if first_word.upper() == second_word.upper():
        return True
    else:
        return False
    
#introduce program
print("Welcome to guess the longest word!")
print("="*30)

#loop variable
run_again = 'Y'

# Check what the run_again variable is holding
while run_again == 'Y':
    # Ask for each word - remove any extra white space
    first = input('Please enter a word:').strip()
    second = input('Please enter a second word:').strip()

    # Check if it is the same word, or the same length - and if these both pass - they are different words of different lengths

    if same_word_check(first, second):
        print(f'Please enter new words - they are the same word')

    elif same_length(first, second):
        print(f'These words are the same length - {len(first)} characters.')
    else:
        long, short = longest_word(first, second)
        print(f'The longest word is {long} and {short} is the shortest.')
    
    # Modify the loop variable by asking again - send the result to uppercase so that y or n work
    run_again = input('Would you like to check two more words? (Y/N):').upper()

#thank the user
print("Thank you for playing")

