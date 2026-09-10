import random
import string


print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

if length < 4:
    print("Password length must be at least 4.")

else:
    uppercase = input("Include uppercase letters? (y/n): ").lower()
    lowercase = input("Include lowercase letters? (y/n): ").lower()
    numbers = input("Include numbers? (y/n): ").lower()
    special = input("Include special characters? (y/n): ").lower()

    characters = ""

    if uppercase == "y":
        characters += string.ascii_uppercase

    if lowercase == "y":
        characters += string.ascii_lowercase

    if numbers == "y":
        characters += string.digits

    if special == "y":
        characters += string.punctuation

    if characters == "":
        print("You must select at least one character type.")

    else:
        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)