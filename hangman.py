from random_word import RandomWords


def posible_exit():
    option = input("\nIf you want to exit the game press 'X': ")
    if (option == "X"):
        exit()
    print("\n")

def choose_dificulty():
    while(True):
        option = input('''
Choose a dificulty:
    1) Easy game: 20 attempts
    2) Normal game: 16 attempts
    3) Hard game: 12 attempts
    4) Imposible game: 10 attempts
    
Choose the option: ''')
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
    if character in actual_word:
        return actual_word, -1
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
            file_name = input("Put the file with that contains the words: ")
            with open(file_name,"r") as file:
                lines = file.readlines()
                words = [line.strip().upper() for line in lines]
                break
        except FileNotFoundError:
            print("The file cannot be read")
    return len(words), words

def create_results_player(results):
    file_name = input("Put the file where is gonna save the results (don't put .txt): ")
    with open(f"results/{file_name}.txt","w") as file:
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

def create_results_machine(results):
    file_name = input("Put the file where is gonna save the results (don't put .txt): ")
    with open(f"results/{file_name}.txt","w") as file:
        for result in results[:-1]:
            word,local_attempts,solved = result
            if (solved):
                file.write(f"The machine has guessed the {word}. It used {local_attempts} attempts.\n")
            else:
                file.write(f"The machine has failed the word {word}.\n")

        last_result = results[-1]  
        if isinstance(last_result, tuple) and len(last_result) == 3:
            nWords,correct,total_attempts = last_result
            file.write(f"Out of {nWords} words, the machine solved {correct} and failed in {nWords-correct}. Used {total_attempts} attempts.\n")
        else:
            print("Unexpected format for last result:", last_result)


def game_playerVsMachine(dificulty,words, nWords):
    count = 1
    correct = 0
    incorrect = 0
    attempts = 0
    results = []

    for word in words:
        posible_exit()
        print(f"This is the word number {count} to be guessed.\n")
        print(word)
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
            if number_character_in_word > 0:
                character_correct += number_character_in_word
                print(f"\nThe character '{character}' apperars {number_character_in_word} times in the word.\n")
            elif number_character_in_word == 0:
                print(f"\nThe letter {character} is not in the word.\n")
            else:
                print(f"\nYou have repeated the letter.\n")
                attempts -= 1
                local_attempts -= 1
            
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

        results.append((word,actual_word,local_attempts,solved))
        count += 1

    results.append((nWords,correct,incorrect,attempts))
    create_results_player(results)

def game_machineVsMachine(dificulty,words,nWords):
    alphabet = ["E", "T", "A", "O", "I", "N", "S", "H", "R", "D", "L", "C", "U", "M", "W", "F", "G", "Y", "P", "B", "V", "K", "J", "X", "Q", "Z"]            
    total_attempts = 0
    local_attempts = 0
    solved = False
    results = []
    correct = 0

    for word in words:
        word_str = word
        word = set(word)
        local_attempts = 0

        for letter in alphabet:
            if local_attempts == dificulty:
                solved = False
                break
            word.discard(letter)
            local_attempts += 1
            total_attempts += 1
            if (len(word) == 0):
                solved = True
                correct += 1
                break
        results.append((word_str,local_attempts,solved))
    
    results.append((nWords,correct,total_attempts))
    create_results_machine(results)



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
Introduce the option: ''')
    if (option == "1"):
        playerVsMachine_option1(choose_dificulty())
    elif (option == "2"):
        playerVsMachine_option2(choose_dificulty())
    else:
        exit()

def machineVsMachine_option1(dificulty):
    nWords: int = numberWords()
    words = getRandomWords(nWords)
    game_machineVsMachine(dificulty,words,nWords)

def machineVsMachine_option2(dificulty):
    nWords, words = open_file()           
    game_machineVsMachine(dificulty,words,nWords)

def machineVsMachine():
    option = input('''
Do you want to the machine uses random words or you want to use a file?
        1) RANDOM WORDS
        2) FROM A FILE

If you want to exit, press other character.
Introduce the option: ''')
    if (option == "1"):
        machineVsMachine_option1(choose_dificulty())
    elif (option == "2"):
        machineVsMachine_option2(choose_dificulty())
    else:
        exit()



while (True):
    try:
        option = input('''
Select one option to play the hangman game:
                
    1) Play against the machine.
        - No look the words
        - You have 3 modes to play:
                -> Easy game: 20 attempts
                -> Normal game: 16 attempts
                -> Hard game: 12 attempts
                -> Imposible game: 10 attempts
                
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