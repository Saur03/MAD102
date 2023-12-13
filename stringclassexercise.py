# Program Name: Password verification program
# Purpose: Determine if the password is the correct number of characters (10) and just letters and numbers
# Author: Richard Grayson
# Date completed: September 2023


# declare function
def verify_password(password):
    # Check if the passed string has 10 or more characters
    if len(password) >= 10:
        # Check if it is just letters and numbers - no special characters (!, # %, etc.)
        if password.isalnum():
            return True
        else:
            print(f'Your password contains incorrect characters.')
            return False
    else:
        print(f'Your password is too short.')
        return False
    

# introduce the program
print('Welcome to the password verification system')
print('=='*30)

#get the potential password
password = input('Please enter your password for verification:')

# Check that the password is good
if verify_password(password):
    print(f'Your password is valid: {password}')
else:
    print(f'{password} cannot be used')

# thank the user
print('Thank you for using my program.')