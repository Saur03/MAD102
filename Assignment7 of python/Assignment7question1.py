'''
Question1- Create a class that will model a Food.  It will have a property for a name, a category (Meat, Canned Soup, Dairy, Spreads, etc.) it will have a retail price (5.99), 
it will have a weight in grams (25.2) and it will have an aisle number where it can be found (5, 23, etc.).  
It will have a method that will describe the food and include details about every property.  
For example - "We have 25.4 g containers of the dairy product Nacho Cheese that retails for $5.99 and can be found in aisle 45."  
The bold text represents the properties - your output does not require bold text, this is just to demonstrate your method details.
Create an instance of this food -  Heinz Baked Beans in 400 g cans located in aisle 23 in the category of Canned Vegetables for $1.06 a can.  Once you have created the instance, call the method.
Create an instance of this food - Kraft Peanut Butter in 1000g container.  This is located in the with the Spreads in aisle 6 for $5.77 each.   Once you have created this instance, call the method.
'''
# Program name:- Food Model Program
# Program Purpose:- To create a class and call its instances    
# Name:- Saurabh Chawla
# Date:- 3 November 2023

# Program Introduction
print('Welcome to our first OOPS program')

# Creating the class that is model a food
class foodModel:
    def __init__(self, name, category, retailPrice, weight, aisleNumber):
        self.name = name
        self.category = category
        self.retailPrice = retailPrice
        self.weight = weight
        self.aisleNumber = aisleNumber

    # Creating a method that describe the food and include details about every property    
    def description(self):
        print(f'We have {self.weight} g containers of the {self.category} product {self.name} that $ {self.retailPrice} and can be found in {self.aisleNumber}. ')

# Creating an instance of the food - Heinz Baked Beans
heinzBakedBeans = foodModel('Heinz Baked Beans', 'Canned Vegetables', 1.06, 400, 23 )
heinzBakedBeans.description()

# Creating an instance of the food - Kraft Peanut Butter
kraftPeanutButter = foodModel('Kraft Peanut Butter', 'Spreads', 5.77, 1000, 6)
kraftPeanutButter.description()

# Thank the user
print('Thank you for using our program')