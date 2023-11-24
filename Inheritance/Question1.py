'''
QUESTION 1
Step 1:
Create a class called Person - it will have the following details:
name
date of birth
It can do the following - introduce itself with its name and date of birth

Step 2:
Create a class called Manager - it shares the following details with a person
name
date of birth
But it also has a date employed and a department that they manage.
It can also introduce itself (using the same method as a Person) and it can add what the department name they manage in.

Step 3:
Create a class called Employee - it shares the same details as a person but it also has a date of hire.  It has the same introduction behavour.

Step 4:
Create a list that will hold some Person objects - you do not have to request the information - just create them with literal values.
Create 2 people with a name and birthdate of your choice - add them to your list.
Create 1 manager with all the details of your choice - add them to your list.
Create 2 employees with all the details of your choice - add them to your list.

Step 5:
Once you have added them to your list - using code, loop through the list, calling their introduction method.
'''


#Program: Inheritance program
#Purpose: To make 3 classes and using inheritance 
#Name: Saurabh Chawla
#Date: 24 November 2023

#Create a Person class
class Person:
    def __init__(self, name, dateOfBirth):
        self.name = name
        self.dateOfBirth = dateOfBirth

    def introduce(self):
        print(f'My name is {self.name} and my date of birth is: {self.dateOfBirth}. ')

#Create a Manager class
class Manager(Person):
    def __init__(self, name, dateOfBirth, dateEmployed, department):
        super().__init__(name, dateOfBirth)
        self.dateEmployed = dateEmployed
        self.department = department

    def introduce(self):
        Person.introduce(self)
        print(f'I am in this department: {self.department}. ')

# Create an Employee class
class Employee(Person):
    def __init__(self, name, dateOfBirth, dateOfHire):
        super().__init__(name, dateOfBirth)
        self.dateOfHire = dateOfHire

    def introduce(self):
        print(f'I hire employees on this date: {self.dateOfHire}. ')
        Person.introduce(self)
        

# Welcome to our program
print('Welcome to our program. ')

personList = []

# created 2 instances for Person class
p1 = Person("Saurabh", "1997-05-03")
p2 = Person("Mayank", "1994-09-05")

# created 1 instance for Manager class
m1 = Manager("Sakshi", "1972-10-25", "1990-08-03", "HR" )

# created 2 instances for Employee class
e1 = Employee("Varun", "2002-06-02", "2021-09-08")
e2 = Employee("Dinesh", "1998-01-09", "2019-08-31")

personList.append(p1)
personList.append(p2)
personList.append(m1)
personList.append(e1)
personList.append(e2)



for person in personList:
    person.introduce()

# Thank the user
print('Thank you for using our program') 
