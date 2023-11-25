'''
QUESTION 2

Create the following classes:

A class for a town.   It will have a name and a population value.  It will also have a method that displays the name and current population.

A class for a monster.  It will have name and a town value.  It will have a method that introduces itself, displaying the name.  It will also have a method called attack.  
This method will display the words ' I am attacking ' and the name of its town.  It will then decrease the population by one person.

Create a program that will ask the user for information to create a town.  Ensure that if the user enters a non-numeric value for the population, it will not crash.    
Then create a new monster and assign this town.  Call all the methods for the monster.

'''

#Program: Population and Town Program
#Purpose: To check whether the user enter numeric value or not and decrement the population by 1, if the user enter numeric value..
#Name: Saurabh Chawla
#Date: 24 November 2023


# Created the town class
class Town:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def description(self):
        print(f'The town name is {self.name} and its population is {self.population}. ')


# Created the monster class
class Monster:
    def __init__(self, monsterName, town):
        self.monsterName = monsterName
        self.town = town

    def introduce(self):
        print(f'I am {self.monsterName}. ')

    def attack(self):
        print(f'I am attacking and {self.town.name}. ')
        self.town.population -= 1

# Introduction
print('Welcome to our town and population program!')

# Ask the user to enter the town name
townName = input('Enter the town name: ')

#checking the condition, if the user enters a non-numeric value for the population, it will not crash.
while True:
    try:
        population = int(input('Enter the population: '))
        break
    except ValueError:
        print('Invalid population! Please enter numeric value. ')


town = Town(townName, population)

# create a new monster and assign this town.  Call all the methods for the monster.
newMonster = Monster("saurabh", town)
newMonster.introduce()
newMonster.attack()

newMonster.town.description()

#Thank the user
print('Thank you for using our program. ')



