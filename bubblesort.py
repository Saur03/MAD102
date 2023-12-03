import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
random.shuffle(letters)

print(letters)

print('Welcome to our bubble sort')

last_letter_index = len(letters) - 1

while last_letter_index >= 0:
    print(f'The last letter index is {last_letter_index}')

    for index in range(last_letter_index):
        if letters[index] > letters[index + 1]:
            temp = letters[index]
            letters[index] = letters[index + 1]
            letters[index + 1] = temp
        print(letters)

    last_letter_index -= 1

print('Sorted')
print(letters)