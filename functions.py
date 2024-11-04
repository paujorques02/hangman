from random_word import RandomWords

def posible_exit():
    # Prompt the user to exit the game by pressing 'X'
    option = input("\nIf you want to exit the game press 'X': ")
    if (option == "X"):
        exit()
    print("\n")

def choose_dificulty():
    # Loop to prompt for a difficulty level until a valid option is entered
    while(True):
        option = input('''
Choose a dificulty:
    1) Easy game: 20 attempts
    2) Normal game: 16 attempts
    3) Hard game: 12 attempts
    4) Imposible game: 10 attempts
    
Choose the option: ''')

        # Return the number of attempts based on the difficulty level
        if option=="1":
            return 20
        elif option == "2":
            return 16
        elif option == "3":
            return 12
        elif option =="4":
            return 10
        print("Incorrect option")

def getRandomWords(nWords: int):
    # Generate a list of random words in uppercase for the game
    r = RandomWords()
    words = []
    for _ in range(nWords):
        words.append(r.get_random_word().upper())
    return words

def numberWords():
    # Prompt the user to enter the number of words to play
    while(True):
        try:
            nWords: int = int(input("How many words do you want to play? "))
            break
        except ValueError:
            print("Introduce a number.")
    return nWords

def is_in_Word(actual_word, final_word, character):
    # Checks if a character is in the target word and updates the guessed word
    if character in actual_word:
        return actual_word, -1  # Return unchanged word if character was already guessed
    if final_word.count(character) == 0:
        return actual_word, 0   # Character is not in the word
    
    # Update guessed word if character is in the final word
    new_word = list(actual_word.split())
    index = 0
    for attempt_character in final_word:
        if attempt_character == character:
            new_word[index] = character
        index += 1
    new_word_str = ' '.join(new_word)
    return new_word_str, final_word.count(character)