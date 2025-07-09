import random
import string
import pyperclip 

def generate_password(length, use_special, use_digits):
    characters = list(string.ascii_letters)  # A-Z and a-z

    if use_digits:
        characters += list(string.digits)
    if use_special:
        characters += list(string.punctuation)

    if not characters:
        return "Error: No characters selected for password generation."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_to_file(password, filename="passwords.txt"):
    with open(filename, "a") as f:
        f.write(password + "\n")
    print(f"Password saved to {filename}.")

def main():
    print("=== PASSWORD GENERATOR TOOL ===")
    try:
        length = int(input("Enter password length: "))
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    password = generate_password(length, use_special, use_digits)
    print("\nGenerated Password:\n" + password)

    choice = input("\nSave password to file? (y/n): ").lower()
    if choice == 'y':
        save_to_file(password)

    try:
        choice = input("Copy to clipboard? (y/n): ").lower()
        if choice == 'y':
            pyperclip.copy(password)
            print("Password copied to clipboard Enjoy!")
    except:
        print("Error")

if __name__ == "__main__":
    main()
