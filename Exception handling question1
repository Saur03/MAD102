'''
QUESTION 1

Here are some provinces and their capital cities:

provinces_and_capitals = { 'Newfoundland And Labrador': 'St Johns' ,
  'Prince Edward Island':'Charlottetown' ,
  'Nova Scotia':'Halifax' ,
  'New Brunswick':'Fredericton' ,
  'Quebec':'Quebec City',
  'Ontario':'Toronto' ,
  'Manitoba':'Winnipeg' ,
  'Saskatchewan':'Regina' ,
  'Alberta':'Edmonton' ,
  'British Columbia':'Victoria' ,
  'Nunavut':'Iqaluit' ,
  'Northwest Territories':'Yellowknife' ,
  'Yukon':'Whitehorse' }

Create a program that will ask the user for a province and it will look up the associated capital city.  

If the province is found, it will display a message telling the user the city for the province.  Here is an example of the input and the results:

Please enter a province to look up it's capital city or X to quit: ontario
Toronto is the capital for Ontario.

If the province is not found, a KeyError will be displayed.  Make sure that you handle this exception, it will display this message:

Please enter a province to look up it's capital city or X to quit: tattoine

Tattoine could not be found
'''


# Program Name: Provinces and Capitals program
# Purpose: To check whether the user have entered the correct provinces and capitals or not and also checking the exception handling
# Author: Saurabh Chawla
# Date: 19 November 2023

# Program Introduction
print('Welcome to the quiz game of provinces and Capital city')

provinces_and_capitals = {'Newfoundland And Labrador': 'St Johns',
                     'Prince Edward Island': 'Charlottetown',
                     'Nova Scotia': 'Halifax',
                     'New Brunswick': 'Fredericton',
                     'Quebec': 'Quebec City',
                     'Ontario': 'Toronto',
                     'Manitoba': 'Winnipeg',
                     'Saskatchewan': 'Regina',
                     'Alberta': 'Edmonton',
                     'British Columbia': 'Victoria',
                     'Nunavut': 'Iqaluit',
                     'Northwest Territories': 'Yellowknife',
                     'Yukon': 'Whitehorse'
                     }

provinces = []

for province in provinces_and_capitals.values():
    provinces.append(province)

while True:
    user = input(f'Please enter a province to look up its capital city or X to quit: ').strip().title()

    if user == 'X':
        break
    
    try:
        capitals = provinces_and_capitals[user]
        print(f'{capitals} is the capital of {user}. ')

    except KeyError:
        print(f'{user} could not be found')

# Thank the user
print(f'Thank you for using our program')