import string
import random

def get_user_input():
    while True:
        try:
            characters_number = int(input("Choose the length of your password: "))
            if characters_number < 5:
                print("Your number should be at least 5.")
            else:
                return characters_number
        except ValueError:
            print("Please enter numbers only.")

def generate_password(length, uppercase, lowercase, numbers, special_chars):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: Please select at least one character type.")
        return None

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password

def main():
    print("Welcome to My Random Password Generator")

    while True:
        try:
            length = int(input("Choose the password length: "))
            if length < 5:
                print("Password length should be at least 5.")
            else:
                break
        except ValueError:
            print("Please enter numbers only.")

    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, uppercase, lowercase, numbers, special_chars)

    if password:
        print("Generated Password:", password)


main()
