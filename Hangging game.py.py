import random

def play_hangman():
    # Predefined list of 5 words
    words = ["python", "variable", "developer", "server", "database"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to text-based Hangman!")
    
    while attempts > 0:
        # Build the masked word using a list comprehension
        display = "".join([char if char in guessed_letters else "_" for char in word])
        print(f"\nWord: {display}")
        print(f"Attempts remaining: {attempts}")
        
        # Win condition
        if "_" not in display:
            print("Congratulations! You guessed the word correctly!")
            break
            
        guess = input("Guess a letter: ").lower().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Correct guess!")
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("Incorrect guess.")
            
    # Loss condition
    if attempts == 0:
        print(f"\nGame over! You ran out of attempts. The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()