import random

print('                Welcome to gaming hangman!\n')
print('Try to guess the word about gaming before running out of attemps!')
print('-----------------------------------------------------------------')
difficulty = input('Choose a difficulty Easy Normal or Difficult (e/n/d):')



wordDictionaryEasy = ['game', 'controller', 'level', 'player', 'score', 'mario', 'jump', 'pixel', 'arcade', 'power', 'bonus', 'quest', 'health', 'coin', 'boss', 'loot', 'cheat', 'speed', 'action', 'adventure']

wordDictionaryNormal = ['console', 'keyboard', 'mouse', 'graphics', 'character', 'strategy', 'online', 'platformer', 'virtual', 'multiplayer', 'resolution', 'upgrade', 'glitch', 'sandbox', 'expansion', 'unlock', 'community', 'tutorial', 'cooperative', 'retro']

wordDictionaryHard = ['esports', 'microtransaction', 'augmented', 'cyberpunk', 'battleroyale', 'vrheadset', 'metaverse', 'speedrun', 'peripheral', 'immersive', 'blockchain', 'indie', 'easteregg', 'modding', 'procedural', 'simulation', 'real-time', 'gameengine', 'speedrunning', 'roguelike']


# Choose a random world on each difficulty
while True:    
    if difficulty == 'e':
        randomWord = random.choice(wordDictionaryEasy)
        break
    elif difficulty == 'n':
        randomWord = random.choice(wordDictionaryNormal)
        break
    elif difficulty == 'd':
        randomWord = random.choice(wordDictionaryHard)
        break
    else:
        print('Choose a difficulty!')
        difficulty = input('Choose a difficulty Easy Normal or Difficult (e/n/d):')


# Prints hangman in every state
def print_hangman(wrong):
    if(wrong == 0):
       print('\n+---+')
       print('    |')
       print('    |')
       print('    |')
       print('   ===')
    elif (wrong == 1):
        print('\n+---+')
        print('O   |')
        print('    |')
        print('    |')
        print('   ===')
    elif (wrong == 2):
        print('\n+---+')
        print(' o  |')
        print('|   |')
        print('    |')
        print('   ===')
    elif (wrong == 3):
        print('\n+---+')
        print(' o  |')
        print('/|  |')
        print('    |')
        print('   ===')
    elif (wrong == 4):
        print('\n+---+')
        print(' o  |')
        print('/|7 |')
        print('    |')
        print('   ===')
    elif (wrong == 5):
        print('\n+---+')
        print(' o  |')
        print('/|7 |')
        print('/   |')
        print('   ===')
    elif (wrong == 6):
        print('\n+---+')
        print(' o  |')
        print('/|7 |')
        print('/ L |')
        print('   ===')

print_hangman(0)

# Prints lines
for i in randomWord:
    print('_', end=' ')


# Check if the letter is right and prints it

def printWord(guessedLetter):
    counter = 0
    rightLetters = 0
    for char in randomWord:
        if(char in guessedLetter):
            print(randomWord[counter], end=' ')
            rightLetters = rightLetters + 1
        else:
            print(' ', end=' ')
        counter = counter + 1
    return rightLetters

def printLines():
    print('\r')
    for char in randomWord:
        print('\u203E', end=" ")

length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0


while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
  print("\nLetters guessed so far: ")
  for letter in current_letters_guessed:
    print(letter, end=" ")
  ### Prompt user for input
  letterGuessed = input("\nGuess a letter: ")
  ### User is right
  if(letterGuessed in randomWord):
    print_hangman(amount_of_times_wrong)
    ### Print word
    current_letters_guessed.append(letterGuessed)
    current_letters_right = printWord(current_letters_guessed)
    printLines()
  ### User was wrong 
  else:
    amount_of_times_wrong+=1
    current_letters_guessed.append(letterGuessed)
    ### Update the drawing
    print_hangman(amount_of_times_wrong)
    ### Print word
    current_letters_right = printWord(current_letters_guessed)
    printLines()

if (amount_of_times_wrong == 6):
    print('\nThe word was: ' + randomWord)
else:
    print('\nYou won!!')

print('Game is over! Thank you for playing!')
