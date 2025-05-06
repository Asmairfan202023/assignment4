import random

def choose_word():
    words = ["python", "computer", "programming", "developer", "hangman", "keyboard", "internet"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])
#hangman game
def play_hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                return
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
        
    print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()
