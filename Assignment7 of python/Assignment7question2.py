'''
Create a class for a Musical Instrument.  It will have the following details:
Three properties of your choice
Two methods - one method can do anything you think is appropriate.  The second method has to use all of the properties you assigned in a descriptive way.
Once you have created the class - create three separate and different instances.  Call both methods on the object.
'''

# Program name:- Food Model Program
# Program Purpose:- To create a class and call its instances    
# Name:- Saurabh Chawla
# Date:- 3 November 2023

# Program Introduction
print('Welcome to our Musical Instruction program')

# Creating the class that is Musical Instrument
class musicalInstrument:
    def __init__(self, name, family, sound):
        self.name = name
        self.family = family
        self.sound = sound
     
     # creating a method of playing instruments   
    def play(self):
        print(f'lets play this instrument{self.play} and it has this sound {self.sound}. ')
     
    # creating a method of properties of instrument in a descriptive way    
    def propertiesDescription(self):
        print(f'The name {self.name} of this instrument {self.family} and it has this {self.sound} sound. ')
        
         
# Creating three separate and different instances and calling both methods 
guitar = musicalInstrument('Guitar', 'String','Versatile')
guitar.play()
guitar.propertiesDescription()

flute = musicalInstrument('Flute', 'Woodwing', 'ethereal')
flute.play()
flute.propertiesDescription()

drum = musicalInstrument('Drum', 'Percussion', 'Percussive')
drum.play()
drum.propertiesDescription()

# Thank the user
print('Thank you for using our program')
