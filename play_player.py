from files import open_file, create_results_player
from functions import *

def playerVsMachine_option1(dificulty):
    # Get number of words from the user and play with random words
    nWords: int = numberWords()
    words = getRandomWords(nWords)
    game_playerVsMachine(dificulty,words,nWords)


def playerVsMachine_option2(dificulty):
    # Get words from file and play
    nWords, words = open_file()           
    game_playerVsMachine(dificulty,words,nWords)

def playerVsMachine():
    # Menu to select word source for player vs machine mode
    option = input('''
Do you want to the machine uses random words or you want to use a file?
        1) RANDOM WORDS
        2) FROM A FILE

If you want to exit, press other character.
Introduce the option: ''')
    if (option == "1"):
        playerVsMachine_option1(choose_dificulty())
    elif (option == "2"):
        playerVsMachine_option2(choose_dificulty())
    else:
        exit()


def game_playerVsMachine(dificulty,words, nWords):
    # Game loop for player vs machine mode
    count = 1
    correct = 0
    incorrect = 0
    attempts = 0
    results = []

    for word in words:
        posible_exit()  # Allow user to exit anytime
        print(f"This is the word number {count} to be guessed.\n")
        character_correct = 0
        local_attempts = 0
        solved = False
        actual_word = "_ " * len(word)
        print(f"You have {dificulty}  attempts to guess the word.\n")
        print(f"Your current word is: {actual_word}")

        for _ in range(dificulty):
            character = input("Introduce a letter: ").upper()
            while not character.isalpha() or len(character) != 1:
                print("\nYou should introduce a single letter.\n")
                character = input("Introduce a letter: ").upper()
            actual_word, number_character_in_word = is_in_Word(actual_word,word,character)
            
            # Update game progress
            if number_character_in_word > 0:
                character_correct += number_character_in_word
                print(f"\nThe character '{character}' apperars {number_character_in_word} times in the word.\n")
            elif number_character_in_word == 0:
                print(f"\nThe letter {character} is not in the word.\n")
            else:
                print(f"\nYou have repeated the letter.\n")
                attempts -= 1
                local_attempts -= 1
            
            print(f"You have {dificulty-local_attempts-1} attempts left.\n")
            print(f"Current word is: {actual_word}")
            local_attempts += 1
            attempts += 1

            if character_correct == len(word.replace(" ","")):
                solved = True
                correct += 1
                print(f"\nYou have guessed the word {word}\n")
                break

        if (not solved):
            print(f"\nSorry, you didn't guess the word {word}\n")
            incorrect += 1

        # Update results
        results.append((word,actual_word,local_attempts,solved))
        count += 1

    results.append((nWords,correct,incorrect,attempts))
    create_results_player(results)
