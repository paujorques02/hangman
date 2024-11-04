def open_file(): 
    # Continuously prompt for a file name until a valid file is provided
    while(True):
        try:
            file_name = input("Put the file with that contains the words: ")
            with open(file_name,"r") as file:
                lines = file.readlines()
                # Read words from the file, convert to uppercase, and remove whitespace
                words = [line.strip().upper() for line in lines]
                break
        except FileNotFoundError:
            print("The file cannot be read")
    return len(words), words # Return word count and list of words

def create_results_player(results):
    # Prompt the user to provide a file name to save results (without ".txt")
    file_name = input("Put the file where is gonna save the results (don't put .txt): ")
    with open(f"results/{file_name}.txt","w") as file:
        for result in results[:-1]:
            word,actual_word,local_attempts,solved = result
            # Write result for each word attempted
            if (solved):
                file.write(f"The word to guess was {word}. You solved in {local_attempts}.\n")
            else:
                file.write(f"You failed. You had {actual_word}, and the word is {word}.\n")

        last_result = results[-1]
        # Write summary of game results 
        if isinstance(last_result, tuple) and len(last_result) == 4:
            nWords, correct, incorrect, attempts = last_result
            file.write(f"Out of {nWords} words, you solved {correct} and failed in {incorrect}. You used {attempts} attempts.\n")
        else:
            print("Unexpected format for last result:", last_result)

def create_results_machine(results):
    # Similar to player results, but records the machine's attempts and results
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