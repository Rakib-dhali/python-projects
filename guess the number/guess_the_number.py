# number guessing game by Rakib Dhali
import random as rd

print("Welcome to the Number Guessing Game!")

while True:
    n = rd.randint(1, 100)
    guesses = 0

    print("\nI've chosen a secret number between 1 and 100. Try to guess it!")

    while True:
        try:
            a = int(input('Guess the number: '))
            diff = abs(a - n)

            if not 1 <= a <= 100:
                print("Please enter a number between 1 and 100.")
                continue

            guesses += 1

            if a < n:
                if diff <= 5:
                    print('Very close. Higher number please')
                else:
                    print('Too low. Higher number please')
            elif a > n:
                if diff <= 5:
                    print('Very close. Lower number please')
                else:
                    print('Too high. Lower number please')
            else:
                print(f'Congrats 🎉 You have guessed the number {n} correctly in {guesses} attempts.')
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Ask to play again
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye.")
        break
