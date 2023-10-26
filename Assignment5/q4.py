
# Program Name: enter the multiple sentences of string and do some string functions 
# Purpose: To print the string in such a way that first letter for each sentence is capitalized and all other letters are lowercased.
# Author: Saurabh Chawla
# Date: 24 October 2023

# Program Introduction
print('Welcome to string function program')

sentence = input('Enter the string of multiple sentences: ')

if(sentence.endswith('.')):
    sentence = sentence[:-1]
many_sentences = sentence.split('.')

for i in range(len(many_sentences)):
    new_line = many_sentences[i].lower().strip().capitalize() + '.'
    print(new_line)

# Thank the user
print('Thank you for using our program')