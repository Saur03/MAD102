'''
Question1:- We are running a copy business.  We want keep track of the number of printing defects we have each day.  
We have three category of defects with their respective codes - misprint (M), misalign (A), blurry (B).  
We want to create a program that we can use througout the day.  
As we encounter a defect, we will enter the defect code.  
We will continue to use this program until the end of the day has been reached.  
We will then enter F to see the final report.  
The program will print out a display of the total (sum) for each defect code.  
It could be that we have a really good day and have no defects in certain codes or all codes, we still need to display that.  
Create this program with the following requirements:
You must create a function that will do the tally output. It will a parameter that represents each of the defect code totals and will display the results in sentence form.  
There is no return from this function
You must include the proper handling so that if a user enters 'b' or 'B' or ' b   ' (with spaces) - they all will be recognized as being the code for blurry.  
This is not handled through a conditional statement
'''
'''
# Program Name: Copy business program
# Purpose: To find the defect in this business and printing the total for each defect 
# Author: Saurabh Chawla
# Date: 24 October 2023

# Introduction
print('Welcome to copy business program')

def defectCount(misprintCount, misalignCount, blurryCount):
    print(f'Total misprint defects: {misprintCount} ')
    print(f'Total misalign defctss: {misalignCount} ')
    print(f'Total blurry defects: {blurryCount} ')

misprintCount = 0
misalignCount = 0
blurryCount = 0

while True:
    defectCode = input('Enter defect code (M, A, B) or F for final report: ')

    if defectCode.strip.lower() == 'f':
        break

    elif defectCode.strip.lower() == 'm':
        misprintCount += 1

    elif defectCode.strip.lower() == 'a':
        misalignCount += 1

    elif defectCode.strip.lower() == 'b':
        blurryCount += 1

defectCount(misprintCount, misalignCount, blurryCount)

# Thank the user
print('Thank you for using our program')
'''

'''
Question2: Create a program that will ask the user if they want to play the even/odd game.   
If they enter Yes or Y or y, ask them for an integer.  Then ask the user if they would like to see all the even or odd numbers up to that number.  
If the user enters the word 'even', 'e', 'E', or any other word that starts with the letter 'e' (of any case),   
it will display all the numbers from 0 to that ending number - but only ones that are even.  

If the user enters 'odd', 'o', 'O' or any other word that starts with the letter 'o' (of any case), 
it will display all the numbers from 0 to that ending number, but only the odd numbers.  Once done, ask them if they want to play the game again.  

Your program should also ensure that they cannot enter anything other than a number when asked.  
If the user enters No or N or n, tell them you are sorry that they do not want to play the game and end the program.
If they enter any other letter, at the beginning, let them know that they have entered and invalid selection and ask them to enter it once again.


def question2(ar):
    # Program Name: even/odd game
    # Purpose: To display the even and odd numbers and do some operations
    # Author: Saurabh Chawla
    # Date: 24 October 2023

    # Program Introduction
    print('Welcome to even/odd game')

    if __debug__:
        out = []
        playGame = str(ar[0]).lower()
    else:
        input('Do you want to play the even/odd game (Y/N)? ').lower()
    while True:
        if playGame.startswith("n"):
            if __debug__:
                out.append('sorry')
            else:
                print('We are sorry that you do not want to play')                                                         
            break
        
        elif playGame.startswith("y"):
            if __debug__:
                number = int(ar[1])
                evenOdd = str(ar[2]).lower()
            else:
                number = int(input('Enter an integer: '))
                evenOdd = input('Provide input to see the corresponding even or odd numbers up to that number: ').lower()
            if evenOdd.startswith('e'):
                print(f'even number upto {number}: ')
                for i in range(number + 1):
                    if i % 2 == 0:
                        if __debug__:
                            out.append(str(i))
                        else:
                            print(i)
            elif evenOdd.startswith('o'):
                print(f'Odd numbers up to {number}: ')
                for i in range(number + 1):
                    if i % 2 != 0:
                        if __debug__:
                            out.append(str(i))
                        else:
                            print(i)
            else:
                if __debug__:
                    out.append('invalid e/o')
                else:
                    print('Invalid Choice. Please enter even or odd or the corresponding first character.' )

            if __debug__:
                playAgain = str(ar[3]).lower()
            else:
                input('Do you want to play the game(Yes/No)? ').lower()
            if playAgain.startswith("y"):
                if __debug__:
                    ar= [ar[0]] + ar[-3:]
                    out.append('continue')
                continue
            else:
                break
        else:
            if __debug__:
                out.append('invalid')
            else:
                print('Invalid Selection. Please enter again')
            continue 
        
    # Thank the user
    if __debug__:
        out.append('Thanks')
        return out
    else:
        print('Thank you for using our program')
'''

'''
Question3:- Design a program that will ask the user to enter a sentence.  It will then take each word and reverse it - before printing out the sentence again.  
For example - if the sentence was "This is a simple sentence", your program would display "Siht si a elpmis ecnetnes."
'''
'''
def question3(ar):
    # Program Name: Reverse the string
    # Purpose: To print the string in reverse order
    # Author: Saurabh Chawla
    # Date: 24 October 2023

    # Program Introduction
    print('Welcome to reverse string program')

    if __debug__:
        sentence = ar
    else:
        sentence = input('Enter the sentence: ')
    if(sentence.endswith('.')):
        sentence = sentence[:-1]
    word = sentence.split()
    for i in range(len(word)):
        word[i] = word[i][::-1].lower()
    reversedSentence = ' '.join(word).capitalize() + '.'
    if __debug__:
        return str(reversedSentence)
    else:
        print(f'Reversed sentence is: {reversedSentence} ')

    # Thank the user
    print('Thank you for using our program')
'''

'''
Question4:- Create a program that asks the user to enter a string that has multiple sentences.   
The sentences will be a complete mix of lowercase and uppercase letters.   
It will then separate the string into individual sentences - and make sure that the first letter for each sentence is capitalized and all other letters are lowercased.  
For example - if the user entered "HelLo.  ThiS is A StrING with MANY Sentences.  ThIS Is NEat". The program will display:

'Hello.'

"This is a string with many sentences.'

'This is neat.'
'''
def question4(ar):
    # Program Name: enter the multiple sentences of string and do some string functions 
    # Purpose: To print the string in such a way that first letter for each sentence is capitalized and all other letters are lowercased.
    # Author: Saurabh Chawla
    # Date: 24 October 2023

    # Program Introduction
    print('Welcome to string function program')

    if __debug__:
        sentence = ar
    else:
        sentence = input('Enter the string of multiple sentences: ')
    if(sentence.endswith('.')):
        sentence = sentence[:-1]
    many_sentences = sentence.split('.')
    for i in range(len(many_sentences)):
        if __debug__:
            out = many_sentences[i].lower().strip().capitalize() + '.'
            print(out)
        else:
            print(many_sentences[i].lower().capitalize())

    # Thank the user
    print('Thank you for using our program')
    return out


from tests import question4_tests
if __name__ == "__main__":
    tests = question4_tests()
    error_count = 0
    
for i in range(len(tests)):
    test = tests[i]
    if (question4(**test['input']) == test['output']):
        print(f'TESTCASE {i+1}: PASS')
    else:
        error_count += 1
        print(f'TESTCASE {i+1}: FAIL')
print(f'TOTAL ERRORS: {error_count}')