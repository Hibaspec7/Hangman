# Problem Set 1, hangman.py
# Name:HIBA ABBAS,IBRAHIM ALTAF,ABU HURAIRA LIAQAT
# Collaborators:40,30,30
# Time spent:4 TO 5 HOURS

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # Iterate through each character in the secret word
    for char in secret_word:
        # If any character of the secret word is not in the guessed list
        if char not in letters_guessed:
            # The word has not been fully guessed yet
            return False
            
    # If the loop finishes without returning False, all letters were found
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      which letters in secret_word have been guessed so far.
    '''
    # Initialize an empty string to accumulate the result
    guessed_word = ""
    
    # Iterate through each letter in the secret word
    for char in secret_word:
        # If the letter has been guessed, add the letter to the result
        if char in letters_guessed:
            guessed_word += char
        # If the letter has not been guessed, add an underscore followed by a space
        else:
            guessed_word += "_ "
            
    return guessed_word



import string

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # Get all lowercase letters (abcdefghijklmnopqrstuvwxyz)
    all_letters = string.ascii_lowercase
    
    # Initialize an empty string to accumulate the letters not guessed
    available_letters = ""
    
    # Iterate through each letter in the alphabet
    for char in all_letters:
        # If the alphabet letter is NOT in the guessed list, add it to our string
        if char not in letters_guessed:
            available_letters += char
            
    return available_letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    vowels = "aeiou"

    # Initial game start message
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings_remaining} warnings left.")
    print("-" * 15)

    # Game loop continues as long as user has guesses and hasn't won
    while guesses_remaining > 0:
        # Check if the user has successfully guessed the word
        if is_word_guessed(secret_word, letters_guessed):
            unique_letters = len(set(secret_word))
            total_score = guesses_remaining * unique_letters
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {total_score}")
            return

        # Status update for each round
        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        
        user_input = input("Please guess a letter: ").lower()

        # Step 1: Check if input is a valid alphabet character
        if not user_input.isalpha() or len(user_input) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses_remaining -= 1
                print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
        
        # Step 2: Check if the letter was already guessed
        elif user_input in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
        
        # Step 3: Check if guess is correct
        elif user_input in secret_word:
            letters_guessed.append(user_input)
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        
        # Step 4: Handle incorrect guess
        else:
            letters_guessed.append(user_input)
            # Vowels (a, e, i, o, u) cost 2 guesses
            if user_input in vowels:
                guesses_remaining -= 2
            # Consonants cost 1 guess
            else:
                guesses_remaining -= 1
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
        
        print("-" * 15)

    # If loop ends and word not guessed, user loses
    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if my_word matches other_word; False otherwise
    '''
    # Step 1: Remove all spaces from my_word to get the actual length
    # Example: "a_ _ l e" becomes "a__le"
    my_word = my_word.replace(" ", "")
    
    # Step 2: If lengths are different, it's not a match
    if len(my_word) != len(other_word):
        return False
    
    # Step 3: Iterate through each character position
    for i in range(len(my_word)):
        current_char = my_word[i]
        other_char = other_word[i]
        
        # If the character is a letter (already guessed)
        if current_char != '_':
            # It must match the character in the same position of other_word
            if current_char != other_char:
                return False
        
        # If the character is an underscore (not yet guessed)
        else:
            # Important Rule: The hidden letter in 'other_word' cannot be 
            # a letter that the user has already revealed elsewhere in 'my_word'.
            if other_char in my_word:
                return False
                
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
    '''
    # Initialize an empty list to store words that match the pattern
    matches = []
    
    # Iterate through every word in the global wordlist
    for word in wordlist:
        # Use our helper function to check if the word matches the current guess
        if match_with_gaps(my_word, word):
            matches.append(word)
    
    # Check if we found any matches
    if len(matches) == 0:
        print("No matches found")
    else:
        # Join the list of words into a single string separated by spaces and print
        print(" ".join(matches))



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman with a special hint feature (*).
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    vowels = "aeiou"

    # Opening message to the user
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings_remaining} warnings left.")
    print("-" * 15)

    # Continue the game as long as the user has guesses left
    while guesses_remaining > 0:
        # Check if the user has already guessed all the letters correctly
        if is_word_guessed(secret_word, letters_guessed):
            unique_letters = len(set(secret_word))
            total_score = guesses_remaining * unique_letters
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {total_score}")
            return

        # Display status at the start of each round
        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        
        user_input = input("Please guess a letter: ").lower()

        # Hint Logic: If user types '*', show all possible word matches
        if user_input == '*':
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            print("-" * 15)
            continue # No penalty for using a hint

        # Validation: Check if the input is a single alphabetical letter
        if not user_input.isalpha() or len(user_input) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses_remaining -= 1
                print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
        
        # Validation: Check if the user already guessed that letter
        elif user_input in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
        
        # Correct Guess: Letter is in the secret word
        elif user_input in secret_word:
            letters_guessed.append(user_input)
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        
        # Incorrect Guess: Letter is not in the secret word
        else:
            letters_guessed.append(user_input)
            # Penalty: Vowels cost 2 guesses, Consonants cost 1 guess
            if user_input in vowels:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
        
        print("-" * 15)

    # Game Over: User ran out of guesses
    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # Pehle wordlist load hogi (jo file ke top par pehle se likha hai)
    
    # Agar simple Hangman khelna hai:
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    # Agar hints ke saath khelna hai (Part 3):
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
