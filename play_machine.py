from files import open_file, create_results_machine
from functions import numberWords, getRandomWords, choose_dificulty

def machineVsMachine_option1(dificulty):
    # Generate random words based on the number chosen by the user
    nWords: int = numberWords()
    words = getRandomWords(nWords)
    game_machineVsMachine(dificulty,words,nWords)

def machineVsMachine_option2(dificulty):
    # Load words from a user-specified file
    nWords, words = open_file()           
    game_machineVsMachine(dificulty,words,nWords)

def machineVsMachine():
    # Menu for choosing word source for the machine mode
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

def game_machineVsMachine(dificulty,words,nWords):
    # Simulate the machine guessing words from an alphabet-based sequence
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
    
    # Store results summary
    results.append((nWords,correct,total_attempts))
    create_results_machine(results)