'''
Create a program called - Guess the Alkali Metals

Lithium (Li), Sodium (Na), Potassium (K), Rubidium (Rb), Cesium (Cs) and Francium (Fr) are alkali metals.   
Your program will ask the user to guess an alkali metal.  They will enter a value and you will check to see if it is an alkali metal.  
Your program needs to properly handle any inputs (CS, cs, Cs, cS would all be correct entries for Cesium). 

If they guess correctly then you let them know they have guessed one of the metals.  Then display the metals that they did not guess.
If they did not guess any of the correct alkali metals, then let them know they were wrong.  Then display all the metals.
For the toolbar, press ALT+F10 (PC) or ALT+FN+F10 (Mac).
'''
'''
# Program Name: Guess the Alkali Metals
# Purpose: To find whether the alkalimetal is correctly guessed or not
# Author: Saurabh Chawla
# Date: 27 October 2023

# Program Introduction
print('Welcome to Guess the Alkali Metals')

alkaliMetals = ['Li', 'Na', 'Rb', 'Cs', 'Fr']
guessedmetals = []
while True:
    entries = input('Please guess an alkali metals: ').strip().capitalize()
    print(entries)
    for i in alkaliMetals:
        if entries in alkaliMetals:
            print('you have guessed one of the metals')
            alkaliMetals.remove(entries)
            print(alkaliMetals)
            break

        else:
            print('You were wrong')  
            print(alkaliMetals) 

# Thank the user
print('Thank you for using our program')
'''
'''
Here are some provinces and their capital cities:

St. John’s - Newfoundland and Labrador
Charlottetown - Prince Edward Island
Halifax - Nova Scotia
Fredericton - New Brunswick
Quebec City - Quebec
Toronto - Ontario
Winnipeg - Manitoba
Regina - Saskatchewan
Edmonton - Alberta
Victoria - British Columbia
Iqaluit - Nunavut
Yellowknife - Northwest Territories
Whitehorse - Yukon
Create a dictionary that will hold the provinces and their capital cities.

Create an array of just the provinces from the dictionary you created.

Create a quiz game.  
The game will randomly choose a province from your province array and ask the user to enter the capital city.  
If the person correctly enters the capital city, they win the game.  
Otherwise they lose - and display the correct answer to them.  
Your notification of the win or loss must include the capital city as part of the output - correct any issues that the user might have capitalizing the first letter of each word.  
For example - if they entered quebec CIty - your output would read Quebec City.  If they lost, let them know what the correct answer is.
'''
'''
import random
# Program Name: quiz game with province and capital city
# Purpose: To find whether the person enter the capital city correctly guessed or not
# Author: Saurabh Chawla
# Date: 27 October 2023

import random
# Program Introduction
print('Welcome to the quiz game of provinces and Capital city')

provincesCapitals = {'St. John’s':'Newfoundland and Labrador', 
                     'Charlottetown':'Prince Edward Island', 
                     'Halifax':'Nova Scotia', 
                     'Fredericton': 'New Brunswick', 
                     'Quebec City':'Quebec', 
                     'Toronto':'Ontario', 
                     'Winnipeg':'Manitoba', 
                     'Regina':'Saskatchewan', 
                     'Edmonton':'Alberta', 
                     'Victoria':'British Columbia', 
                     'Iqaluit':'Nunavut', 
                     'Yellowknife': 'Northwest Territories', 
                     'Whitehorse':'Yukon' 
                     }
provinces = []

for province in provincesCapitals.values():
    provinces.append(province)

#select the random province
index = random.randint(0,len(provinces))
randomProvince = provinces[index]

for capital in provincesCapitals.keys():
    if provincesCapitals[capital] == randomProvince:
        answer = capital

userAnswer = input(f'What is the capital city of {randomProvince}?: ').lower()

if userAnswer == answer.lower():
    print(f'You won!. The capital city of {randomProvince} is {answer}. ')
else:
    print(f'You lose!. The correct capital city of {randomProvince} is {answer}.')

# Thank the user
print('Thank you for using our program.')            
'''
'''
Question3:- Create a program that will ask a user to enter their favourite movies.  
The program will keep prompting and asking them to enter the names of movies until the user let's you know they are done.  
Error proof your handling of the user input information so that lowercase or uppercase letters are identified (when they want to continue - C or c will work).  
Once completed you will create a formatted output with a heading of 'Movie Collection' 
using a formatted heading similar to what we did with our class exercise files and with the following requirements:

The heading must be in all uppercase letters (DO NOT DO THIS YOURSELF - USE CODE) 
and will include the number of total movies that are going to be displayed.  
For example - 'MOVIE COLLECTION WITH 8 MOVIES' if there were 8 movies the user entered.
The number of underlining characters under your heading will be equal to the longest movie title that was entered.  
HINT: - Create a function that you pass an array of movies to and it will return the number of characters in the longest movie title.
All of the movies will have the first letter of every word captialized - regardless of how the user entered it.
You must include proper commenting follow the structure demonstrated in class.
'''

# Program Name: Favorite Movie program
# Purpose: To find the number of character in the longest movie title and using some functions
# Author: Saurabh Chawla
# Date: 27 October 2023

# define the function
def longestMovieTitle(movies):
    movielength = 0
    for movie in movies:
        length = len(movie) 
        if length > movielength:
            movielength = length
    return movielength

# Program Introduction
print('Favourite movie program')
print("="*40)

# Variable declaration
movies = []
sentinel = 'c'

# Ask the user to enter the favourite movie
while sentinel == 'c':
    user = input('Please enter your favourite movie: ' )
    movies.append(user.title())
    sentinel = input('Enter \'c\' or \'C\' to continue and anything else to exit: ').lower()

totalNumber = len(movies)

underliningCharacters = longestMovieTitle(movies)

print(f'movie collection with {len(movies)} movies'.upper())
print('-'*underliningCharacters)
for movie in movies:
    print(movie)


# Thank the user
print('Thank you for using our program')    