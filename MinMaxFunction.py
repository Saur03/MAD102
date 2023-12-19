
# Declare my min max function
def min_max(score1, score2):
    if score1 < score2:
        return (score1, score2)
    else:
        return (score2, score1)
    
# Declare score differnce function
def score_difference(score1, score2):
    min, max = min_max(score1, score2)
    difference = max - min
    return difference


# Program introduction
print("Welcome to my program")
print("="*30)

# get the scores
score1 = int(input('Please enter the score for player 1:'))
score2 = int(input('Please enter the score for player2:'))

# get the highest score
min, max = min_max(score2, score1)

# Get the difference
difference = score_difference(score1, score2)

# output the results
print(f'The highest score was {max}.')
print(f'The difference between the high score and the min score was {difference}')

# thank the user
print('Thank you for using my program.')
