import random
import string

def generate_password(length, complexity):
    characters = ''

    if 'lowercase' in complexity:
        characters += string.ascii_lowercase
    if 'uppercase' in complexity:
        characters += string.ascii_uppercase
    if 'digits' in complexity:
        characters += string.digits
    if 'special' in complexity:
        characters += string.punctuation

    if not characters:
        print("Please select at least one complexity option.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
        complexity = input("Enter password complexity (lowercase/uppercase/digits/special, separated by commas): ").split(',')

        password = generate_password(length, complexity)

        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid length.")

if __name__ == "__main__":
    main()
