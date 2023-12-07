'''
QUESTION 1:- We are going to create a program that will model a zookeeper and its animals.  
Step 1:
Build a zookeeper class.  This class will have a name and has a list of animals that he is taking care of.  
By default, the zookeeper has no animals when they are first created.  
The zookeeper will have a method that introduces themselves and displays how many animals they are keeping track of.  
They also have a method that will add an animal to their list of animals.
5 marks

Step 2:
Build an animal class.  This class will have a name and age.  It will have a method that describes the animal using its name and age.
3 marks

Step 3:
Build a bird class.  The bird is an animal.  
It will do what an animal does and has the same details.  
It will also have a colour of its feathers and this must be included in its describe method.
4 marks

Step 4: 
Build a fish class.  The fish is an animal. 
It will do what an animal does and has the same details.  
It will also have a colour of its scales and this must be included in its describe method.
4 marks

Step 5:
Create a function that will take in a value - if that value is '1' then it will display 'You chose an animal' in the console with an appropriate underlining.  
If the value is '2' it will display 'You chose a bird' in the console.   
If any other value is entered, it will display 'You chose a fish' in the console with an appropriate underlining.
4 marks

Step 6;
Build a program that has the following steps:
Ask the user to create a new zookeeper.  Ensure that you properly handle and capitalize their name.  
There will only be a single zookeeper.  Once created - call the introduction method.

Ask the user if they want to add some animals.  If they say no - the program is done. 
If they say yes, ask them how many animals they would like to add
Ensure that they enter a valid numerical value - keep asking until they enter a valid number
You need to create however number of animals the user wants.  

For each animal you need to create, ask the user if they want to create a regular animal by entering 1, a bird by entering 2 or fish by entering anything else.  
When you get the value, use your function from step 5 to display the appropriate heading.
Ask for the details to build the desired animal.  Add it to the animals the zookeeper is watching using the appropriate method.
Repeat this process until you are done with the required number the user asked for.

Make sure you include the animal number (i.e. if they asked for three - ask for the details for animal #1, then animal #2 then animal #3)
Once you have completed asking, display the animals that the zookeeper is watching - 
if they are watching no animals, display that they are lonely because they have no animals to watch.

Output must be:- 
Below is a sample of the program running in the console:

Welcome to the St. Clair Zoo
===========================================================================
We need a zookeeper - please create a zookeeper and then introduce them.
Please enter the name for the zookeeper:steve IRWin
Hello! My name is Steve Irwin and I am responsible for 0 animals.
Would you like to add some animals for me to watch?: y/n: y
How many animals should I watch?: r
That is not a valid number - please enter a number
How many animals should I watch?: 2
---------------------------------------------
Press 1 to enter a regular animal 
Press 2 to enter a bird or 
Enter any other value to enter a fish: 1
---------------------------------------------

You chose a regular animal
=======================================================
Please enter the name for animal #1: crocodile Rock
Please enter the age for animal #1: 22
---------------------------------------------
Press 1 to enter a regular animal 
Press 2 to enter a bird or 
Enter any other value to enter a fish: 
---------------------------------------------

You chose a Fish
=======================================================
Please enter the name for animal #2: dory
Please enter the age for animal #2: 9
Please enter the colour of the scales on animal #1: blue
Would you like to add some animals for me to watch? y/n :n

Here are all of the animals that I am watching:
---------------------------------------------
This animal is 22 years old and is names Crocodile Rock.
This animal is 9 years old and is names Dory.
It has beautiful blue scales.
Thank you for using my zookeeper program.
'''

# Program- Animal and Zookeeper program
# Purpose- To display the animals using classes, inheritance and exception handling.
# Name- Saurabh Chawla
# Date- 6 December 2023

# Creating a zookeeper class
class Zookeeper:
    def __init__(self, name, listOfAnimal=[]):
        self.name = name
        self.listOfAnimal = listOfAnimal

    def introduce(self):
        print(f'Hello my name is {self.name} and I am responsible for {len(self.listOfAnimal)} animals. ')

    def addAnAnimal(self, animal):
        self.listOfAnimal.append(animal)

# Creating a Animal class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f'Hello, my name is {self.name} and my age is {self.age}. ')

# Creating a bird class
class Bird(Animal):
    def __init__(self, name, age, feathersColor):
        super().__init__(name, age)
        self.feathersColor = feathersColor

    def describe(self):
        Animal.describe(self)
        print(f'The color of feathers is {self.feathersColor}. ')

# Creating a fish class
class Fish(Animal):
    def __init__(self, name, age, scalesColor):
        super().__init__(name, age)
        self.scalesColor = scalesColor

    def describe(self):
        Animal.describe(self)
        print(f'The color of scales is {self.scalesColor}. ')

# Program Introduction
print('Welcome to the Saint Clair Zoo')
print('='*55)


def displayValue(value):
    if value == '1':
        print('You choose a regular animal. ')
        print('='*45)
    elif value == '2':
        print('You choose a Bird. ')
        print('='*45)
    else:
        print('You choose a Fish. ')
        print('='*45)

while True:
    name = input('Please enter the name for the zookeeper: ').capitalize()
    z1 = Zookeeper(name)
    z1.introduce()

    addSomeAnimals = input('Would you like to add some animals for me to watch?: y/n: ').lower()
    if addSomeAnimals == 'y':
        try:
            number = int(input('How many animals should I watch?: '))
            print('-'*45)
            break
        except ValueError:
            print('That is not a valid number - please enter a number')

for val in range(number):
    
    userInput = input(f'Press 1 to enter a regular animal\n or Press 2 to enter a bird or\n Enter any other value to enter a fish: ')
    print('-'*45)
    displayValue(userInput)

    name = input('Please enter the name for animal: ').strip().title()
    age = int(input('Please enter the age for animal:').strip())

    if userInput == '1':
        animal = Animal(name, age)
    
    elif userInput == '2':
        feathersColor = input('Please enter the colour of the feathers on animal: ')
        animal = Bird(name, age, feathersColor)
    else:
        scalesColor = input('Please enter the colour of the scales on animal: ')
        animal = Fish(name, age, scalesColor)

    z1.addAnAnimal(animal)
    print('Here are all of the animals that I am watching: ')
    print('-'*45)

for animal in z1.listOfAnimal:
    animal.describe()

# Thank the user
print('Thank you for using my zookeeper program.')








        

                