import random
import string

def generate_password(length=12, use_special_chars=True):
    """Generate a random password."""
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    
    # Define the character sets
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    
    generated_password = generate_password(password_length, include_special_chars)
    print(f"Generated Password: {generated_password}")
