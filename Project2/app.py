import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    
    print(f"Think of a number between 1 and {x}, and I'll try to guess it!")
    
    while feedback != "c":
        guess = random.randint(low, high) if low != high else low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"Yay! I guessed your number {guess} correctly!")

# Set the range (e.g., 1 to 100)
computer_guess(100)
