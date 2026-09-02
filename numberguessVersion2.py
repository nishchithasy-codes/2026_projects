import random
while True:
    print("Number guessing game!")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Choose difficulty level (1-3): ")
    if choice == "1":
        max_number = 50
        attempts_allowed =10
    elif choice == "2":
        max_number = 100
        attempts_allowed = 7
    elif choice == "3":
        max_number = 200
        attempts_allowed = 5
    else:
        print("Invalid choice!!")
        continue
    secret_number = random.randint(1,max_number)
    attempts = 0

    print(f"\nI'm thinking of a number between 1 and {max_number}: ")
    print(f"You have {attempts_allowed} attempts.")

    while attempts < attempts_allowed:
        try:
            guess = int(input("Enter your guess number: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1
        if guess < secret_number:
            print("Too Low!")
        elif guess > secret_number:
            print("Too High!")
        else:
            print("🥳CORRECT! you won this game, Hurray!!!!")
            print(f"The number was {secret_number}")
    else:
        print("\nGame Over! You've used all your attempts.")
        print(f"The number was {secret_number}.")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break