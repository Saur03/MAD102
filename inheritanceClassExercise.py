# Create the Person
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    
    def description(self):
        print(f'Name: {self.name} - cell#: {self.phoneNumber} ')

# Create a Student derived class
class Student(Person):
    # Adds a school property - uses the same name and phone number
    def __init__(self, name, phoneNumber, school):
        super().__init__(name, phoneNumber)
        self.school = school

    #Uses the same description method - extends it to add the school - the extension comes after the parent's description method
    def description(self):
        Person.description(self)
        print(f'I attend {self.school}')

# Create an Employee Derived class
class Employee(Person):
    # Adds an employer property - uses the same name and phone number
    def __init__(self, name, phoneNumber, employer):
        super().__init__(name, phoneNumber)
        self.employer = employer

    # Uses the same description method - extends it to add the employer - the extension comes before the parent's description method
    def description(self):
       print(f'Works at {self.employer}')
       Person.description(self)


# Welcome to our program
print('Welcome to our contacts program')
print('-'*55)

# Create an array to hold all the objects
contacts = []

# Ask the user the type of object to create (or Q to quit)
# Add functionality to remove and extra whitespace and properly capitalize the input
type = input('If you want to create a person press P\nIf you want to create a Student press S\nIf you want to create an Employee press E\nPress Q to quit: ').strip().upper()

while type != 'Q':
    # Ask for the name and phone number - properly handle the returned string value by removing whitespace and setting the first letter of each word to uppercase and the remaining to lowercase
    name = input('Please enter the name: ').strip().title()
    cell = input('Please enter your cell number: ').strip()
    
    if type == 'P':   
        # Create a new person object
        person = Person(name, cell)

        # Add it to the contacts array
        contacts.append(person)
    elif type == 'S':
        # Ask for the schoool - properly handle the string
        school = input('Please enter your school name: ').strip().title()

        # Create a new student object
        student = Student(name, cell, school)

        # Add the student to the contacts array
        contacts.append(student)
    elif type == 'E':
        # Ask for the employer - properly handle the string
        employer = input('Please enter the name of your company: ').strip().title()

        # Create a new employee object
        employee = Employee(name, cell, employer)

        # Add the employee to the array
        contacts.append(employee)
    else:
        print('Invalid selection - please choose from one of the following:')

    # Ask the user what they want to do
    type = input('If you want to create another person press P\nIf you want to create another Student press S\nIf you want to create another Employee press E\nPress Q to quit: ').strip().upper()

# Display the results
print('Phone List')
print('='*55)

# Loop through the results and call the description method which exists on every item
for contact in contacts:
    contact.description()

# Thank the user
print('Thanks for using our program')


    