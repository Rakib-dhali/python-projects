import random as rd

while True:
    choice = input("Enter (Y / N): ").lower()

    if choice == "y":
        player_random_number = rd.randint(1, 6)
        computer_random_number = rd.randint(1, 6)
        print(f"You rolled: {player_random_number}, Computer rolled: {computer_random_number}")

        if player_random_number > computer_random_number:
            print("🎉 You win!")
        elif player_random_number < computer_random_number:
            print("💻 Computer wins!")
        else:
            print("🤝 It's a tie!")

    elif choice == "n":
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice, try again.")
