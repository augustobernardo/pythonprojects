'''
    Hangman é um jogo de palavras em que o computador seleciona aleatoriamente uma palavra do dicionário e o jogador deve 
    adivinhá-la corretamente em determinado número de jogadas. A palavra a ser adivinhada é representada por uma fileira de e
    strelas. Se a letra adivinhada estiver presente em palavra, o script será automaticamente colocado nos locais corretos.
'''

import random 
def get_word(): 
    
    words = list(['things', 'way', 'people', 'time', 'place', 'years', 'number', 'school', 'food'])
    selectWords = random.choice(words)
    
    return selectWords 

myword = get_word() 
for i in myword: 
    print("*", end = " ") 

l = len(myword) 
print("\nWord has %d letters" %l) 
def check(myword, your_word, guess1): 
    status = '' 
    matches = 0
    for letter in myword: 
        if letter in your_word: 
            status += letter 
        else: 
            status += '*'
        if letter == guess1: 
            matches += 1

    if matches > 1: 
        print(matches, guess1) 

    elif matches == 1: 
        print(guess1) 
    return status 

def game(): 
    guess = 0
    guessed = False
    your_word = [] 
    turns = len(myword) + 1
    turns1 = turns 

    print("Total turns: ", turns) 
    while guess < turns1: 
        guess1 = input("Enter your guess: ") 
        
        turns -= 1
        
        print("Turns left", turns) 
        
        if guess1 in your_word: 
            print("You already guessed") 
        elif len(guess1) == 1: 
            your_word.append(guess1) 
            result = check(myword, your_word, guess1) 
            if result == myword: 
                guessed = True
                print("You won ") 
                print(myword) 
            else: 
                print(result) 
        else: 
            print("Invalid entry") 
        guess += 1
    if guess == turns1: 
        print("Word is:") 
        print(myword) 
game() 
