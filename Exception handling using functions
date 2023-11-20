'''
QUESTION 2

Create a function that is called item_in_list.  It will take two parameters - one is an index value and the other is a list of items.  
It's function is to search the list and display the results in the console.  
For example, if we passed it in a list of ['Bob','Mary','Joe'] and an index of 2 - it would print 'We found Joe at index position 2'.  
If we passed in an index value of 9, it would display 'An index value of 9 is out of range' - and this error would be based on it seeing an exception for an IndexError.

(5 marks)

Using this function, create a program that will ask the user to enter a sentence.  
It will then ask the user what word they would like to extract - and asks them for a number.  
If the user enters a letter or a number - then it will tell them that the value is not a number because it gave a ValueError.  
Otherwise, it will take the number - and use it to look up which word they are asking about.

For example - I entered this is a simple sentence and then f

Please enter a sentence: this is a simple sentence
Please enter an index position to look up:f
That is not a number - please enter a valid number.

Here is another example - I entered this is a simple sentence and then 3

Please enter a sentence: this is a simple sentence
Please enter an index position to look up:3
We found simple at index 3

Here is another example - I entered this is a simple sentence and then 9

Please enter a sentence: this is a simple sentence
Please enter an index position to look up:9
Sorry - that index value of 9 is out of range.

Note - this does not have to repeat - it only needs to run a single time.  Your program must not crash.
(10 marks)
'''

# Program Name: Index position program
# Purpose: To check the index position using exception handling
# Author: Saurabh Chawla
# Date: 19 November 2023

# Introduction
print('Welcome to index position program')

# Part 1
# Created a function
def item_in_list(indexValue, listOfItems):
    try:
        result = listOfItems[indexValue]
        print(f'We found {result} at index position {indexValue}. ')

    except IndexError:
        print(f'Sorry! An index value of {indexValue} is out of range. ')

List = ['Bob', 'Mary', 'Joe']
item_in_list(2, List)
item_in_list(9, List)


# Part2
user = input('Please enter a sentence: ')
word_list= user.split()

try:
    indexPosition = int(input('Please enter an index position to look up: '))
    item_in_list(indexPosition, word_list)

except ValueError:
    print(f'That is not a number - please enter a valid number.')


# Thank the user
print('Thank you for using our program')                





