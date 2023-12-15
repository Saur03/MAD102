# Create a dictionary
# The dictionary is made up of a key - student name and a value - a dictionary of grades
# The grade dictionary is made up of multiple keys - the course names and  values - each courses grades
students = {'Harry' : {'potions': 88, 'dark arts' :92 } }
students['Ron'] = {'potions': 66, 'dark arts' : 72}
students['Hermione'] = {'dark arts' : 100, 'potions': 100, 'arithmancy': 100}

# the string for the prompt message
menu_message = 'To look up a student, type S \nTo quit type Q:'

# the string for the welcome message - declared as a string so I can use the length for underlines
welcome = 'Welcome to our grade program'

print(welcome)
print('-'*len(welcome))

# ask the user what they want to do and send it to uppercase
choice = input(menu_message).upper()

# create a loop - if the user enters anything but Q, ask for the student name
while choice != 'Q':
    if choice == 'S':
        # ask for a name and send it to uppercase (first letter) and lowercase (all other letters)
        student_name = input('Please enter the student to look up: ').title()

        try:
            # use the student name as a key lookup in the dictionary - if this fails (the name is not in the dictionary)
            # it will throw the exception
            # using the name (key) gets the dictionary of associated values
            grades = students[student_name]
            print('='*30)


            print(f'Grades for {student_name}:')
            # go through each item in the dictionary 
            # assign the key to the course parameter
            # assign the value to the grade parameter
            for course,grade in grades.items():
                print(f'{course.title()} : {grade}%')
        except KeyError: #this error happens if there is not a matching name (key)
            print(f'{student_name} does not exist - please try again.')
        except: #this error covers anything else that happens
            print('Sorry an unknown error as occurred - please try again.')

    # modify the loop variable
    choice = input(menu_message).upper()

#program has ended - thank the user
print('Thank you for using our program')