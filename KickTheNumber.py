'''
    Create a script that generates a value randomly, stores that value, and repeatedly for the user to guess the generated 
    value until he gets it right.
'''
import random

# Start the game
print('KICK THE NUMBER')

# Generating the random number
rand = random.randint(1, 100)

# Catching the user number
userNumber = int(input('Write the right number: '))

# Verify if the number is right
while userNumber != rand:
    guess = int(input('Number wrong, please try again: '))