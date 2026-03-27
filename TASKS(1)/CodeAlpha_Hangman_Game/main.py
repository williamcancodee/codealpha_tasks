import random

def play_hangman():
    # --- SETUP PHASE ---
    # Requirement: Use a small list of 5 predefined words
    words = ["python", "intern", "code", "alpha", "game"]
    
    # Requirement: Randomly select one word
    secret_word = random.choice(words)
    
    # Trackers for game state
    guessed_letters = []
    attempts_left = 6  # Requirement: Limit incorrect guesses to 6
    
    print("Welcome to Hangman!")
    print(f"I have chosen a word. You have {attempts_left} incorrect guesses allowed.")

    # --- GAME LOOP PHASE ---
    # Requirement: Use a while loop to keep the game running
    while attempts_left > 0:
        
        # 1. Display the word with underscores for hidden letters
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word.strip()}")
        
        # 2. Check for Victory
        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            break
        
        # 3. Get User Input
        guess = input("Guess a letter: ").lower()
        
        # 4. Input Validation (Prevent errors)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue
            
        # Add the guess to our history list
        guessed_letters.append(guess)
        
        # 5. Check if the guess is correct (Requirement: If-Else)
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Sorry, '{guess}' is not there. Attempts left: {attempts_left}")
            
    # --- END GAME PHASE ---
    if attempts_left == 0:
        print(f"\nGame Over! The word was: {secret_word}")

# Run the game
if __name__ == "__main__":
    play_hangman()