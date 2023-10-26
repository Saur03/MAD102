# Program Name: Reverse the string
# Purpose: To print the string in reverse order
# Author: Saurabh Chawla
# Date: 24 October 2023

# Program Introduction
print('Welcome to reverse string program')

sentence = input('Enter the sentence: ')
if(sentence.endswith('.')):
    sentence = sentence[:-1]
word = sentence.split()
for i in range(len(word)):
    word[i] = word[i][::-1].lower()
reversedSentence = ' '.join(word).capitalize() + '.'
print(f'Reversed sentence is: {reversedSentence} ')

# Thank the user
print('Thank you for using our program')