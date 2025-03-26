import random
import string

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters")
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure the password meets all criteria
    password = [
        random.choice(upper),
        random.choice(special),
        random.choice(digits)
    ]
    
    # Fill the rest of the password length with random choices from all categories
    all_chars = lower + upper + digits + special
    password += random.choices(all_chars, k=length - 3)
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    return "".join(password)

if __name__ == "__main__":
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    print("Generated Password:", generate_password(length))

