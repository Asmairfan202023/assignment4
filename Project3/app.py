import random

def user_guess(x):
    random_number = random.randint(1, x)
    guess = 0
    
    print(f"I'm thinking of a number between 1 and {x}. Can you guess it?")
    
    while guess != random_number:
        guess = int(input("Enter your guess: "))
        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
    
    print(f"Congratulations! You guessed the number {random_number} correctly!")

# Set the range (e.g., 1 to 100)
user_guess(100)
