import sys
from random_word import RandomWords


def posible_exit():
    option = input("If you want to exit the game press 'X': ")
    if (option == "X"):
        exit()

def choose_dificulty():
    while(True):
        option = input('''
        Choose a dificulty:
            1) Easy game: 12 tries
            2) Normal game: 10 tries
            3) Hard game: 8 tries
            4) Imposible game: 7 tries
''')
        if option=="1":
            return 12
        elif option == "2":
            return 10
        elif option == "3":
            return 8
        elif option =="4":
            return 7
        print("Incorrect option")

def getRandomWords(nWords: int):
    r = RandomWords()
    words = []
    for _ in range(nWords):
        words.append(r.get_random_word().upper())
    return words

def numberWords():
    while(True):
        try:
            nWords: int = int(input("How many words do you want to play? "))
            break
        except ValueError:
            print("Introduce a number.")
    return nWords

def is_in_Word(actual_word, final_word, character):
    if final_word.count(character) == 0:
        return actual_word, 0
    new_word = list(actual_word.split())
    index = 0
    for attempt_character in final_word:
        if attempt_character == character:
            new_word[index] = character
        index += 1
    new_word_str = ' '.join(new_word)
    return new_word_str, final_word.count(character)

def open_file(): 
    while(True):
        try:
            file_name = input("Put the file with the words: ")
            with open(file_name,"r") as file:
                lines = file.readlines()
                words = [line.strip.upper() for line in lines]
                break
        except NameError:
            print("The file cannot be read")
    return len(words), words

def create_results(results):
    with open("results.txt","w") as file:
        for result in results[:-1]:
            word,actual_word,local_attempts,solved = result
            if (solved):
                file.write(f"The word to guess was {word}. You solved in {local_attempts}.\n")
            else:
                file.write(f"You failed. You had {actual_word}, and the word is {word}.\n")

        last_result = results[-1]  
        if isinstance(last_result, tuple) and len(last_result) == 4:
            nWords, correct, incorrect, attempts = last_result
            file.write(f"Out of {nWords} words, you solved {correct} and failed in {incorrect}. You used {attempts} attempts.\n")
        else:
            print("Unexpected format for last result:", last_result)

def game_playerVsMachine(dificulty,words, nWords):
    count = 1
    correct = 0
    incorrect = 0
    attempts = 0
    results = []

    for word in words:
        print(f"This is the word number {count} to be guessed.")
        posible_exit()
        print(word)
        character_correct = 0
        local_attempts = 0
        solved = False
        actual_word = "_ " * len(word)
        print(f"Ok, you have {dificulty}  attempts to guess the word.")
        print(f"Your current word is: {actual_word}")

        for _ in range(dificulty):
            character = input("Introduce a character: ").upper()
            while not character.isalpha() or len(character) != 1:
                print("You should introduce a single character.")
                character = input("Introduce a character: ").upper()
            actual_word, number_character_in_word = is_in_Word(actual_word,word,character)
            if number_character_in_word > 0:
                character_correct += number_character_in_word
                print(f"The character '{character}' apperars {number_character_in_word} times in the word.")
            else:
                print(f"The letter {character} is not in the word.")
            
            print(f"Current word is: {actual_word}")
            local_attempts += 1
            attempts += 1

            if character_correct == len(word.replace(" ","")):
                solved = True
                correct += 1
                print(f"You have guessed the word {word}")
                break

        if (not solved):
            print(f"Sorry, you didn't guess the word {word}")
            incorrect += 1

        results.append((word,actual_word,local_attempts,solved))
        count += 1

    results.append((nWords,correct,incorrect,attempts))
    create_results(results)
            

def playerVsMachine_option1(dificulty):
    nWords: int = numberWords()
    words = getRandomWords(nWords)
    game_playerVsMachine(dificulty,words,nWords)


def playerVsMachine_option2(dificulty):
    nWords, words = open_file()           
    game_playerVsMachine(dificulty,words,nWords)

def playerVsMachine():
    option = input('''
            Do you want to the machine uses random words or you want to use a file?
                   1) RANDOM WORDS
                   2) FROM A FILE

            If you want to exit, press other character.
''')
    if (option == "1"):
        playerVsMachine_option1(choose_dificulty())
    elif (option == "2"):
        playerVsMachine_option2(choose_dificulty())
    else:
        exit()


def machineVsMachine():
    pass



while (True):
    try:
        option = input('''
            Select one option to play the hangman game:
                            
                1) Play against the machine.
                    - No look the words
                    - You have 3 modes to play:
                            -> Easy game: 12 tries
                            -> Normal game: 10 tries
                            -> Hard game: 8 tries
                            -> Imposible game: 7 tries
                            
                2) Machine plays automaticly. You can see how many tries needed to solve the aumount of words that you want.
                            
                X) Exit.
                
                Introduce your option: ''')
        if (option.upper() == "X"):
            exit()
        option: int = int(option)
        break
    except ValueError:
        print('''
              
            You have to introduce a valid value.
               
              ''')
        
if option == 1:
    playerVsMachine()
machineVsMachine()