from play_player import playerVsMachine
from play_machine import machineVsMachine

if __name__ == '__main__':
    # Main menu for choosing game mode or exiting
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
    # Start the selected game mode        
    if option == 1:
        playerVsMachine()
    else:
        machineVsMachine()