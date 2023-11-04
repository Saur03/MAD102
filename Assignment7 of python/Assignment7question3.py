'''
Questiion3:- Create a program that will ask the user to create a number of Instructor objects.  
The Instructor has an office, a first name and a last name.  
The instructor will also have a way of introducing themselves and will display they full name where their office is.  
The user may or may not enter an instructor.  They can enter as many instructors as they want.  
When they are done entering, the program will display all the introductions for every instructor entered.  
If no instructors were entered the program will display that no instructors exist.


Fully comment your code
Make sure that the instructor's name is always properly capitalized
Make sure there are no extra spaces
The user is properly prompted and their answer is always properly handled and accepted.
'''

# Program name:- Instructor Program    
# Program Purpose:-  To check whether the user may or may not entered instructors details correct or not.
# Name:- Saurabh Chawla
# Date:- 3 November 2023

# Program Introduction
print('Welcome to instructor program')

# Creating the class of instructor
class instructor:
    def __init__(self, office, firstName, lastName):
        self.office = office
        self.firstName = firstName
        self.lastName = lastName

    # creating the introduction of the instructor 
    def introducingInstructor(self):
        print(f'Hello I am {self.firstName} {self.lastName} and I am in this room {self.office}. ')

# make an empty list to store Instructor objects
instructors = []
addInstruct = ''

# main program
while addInstruct != 'Q':
    office = input('Enter the instructor office: ')
    firstName = input('Enter the first name of instructor: ').capitalize()
    lastName = input('Enter the last name of instructor: ').capitalize()

    instruct = instructor(office, firstName, lastName)
    # calling methods
    instruct.introducingInstructor()
    instructors.append(instruct)

    addInstruct = input('Hit Enter to add more instructor or Q to quit: ').upper()

# check if the instructors were entered
if not instructors:
    print('No instructors exists. ')
else:
    # displaying all the entered instructors
    print('Here are the instructors')
    for instructor in instructors:
        instructor.introducingInstructor()

# Thank the user
print('Thank you for using our program')    





   


                

