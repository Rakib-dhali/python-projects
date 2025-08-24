import random

options = ['r', 'p', 's']
full_names = {'r': 'rock 🪨', 'p': 'paper 📄', 's': 'scissors ✂️'}

while True:
    com_choice = random.choice(options)
    p_choice = input("\nEnter choice: r (🪨) / p (📄) / s (✂️) or q to quit: ").lower()

    if p_choice == 'q':
        print("👋 Thanks for playing! Goodbye!")
        break

    if p_choice not in options:
        print("❌ Invalid input! Try again.")
        continue

    print(f"👤 Player chose {full_names[p_choice]}, 💻 Computer chose {full_names[com_choice]}")

    if p_choice == com_choice:
        print("🤝 It's a draw!")
    elif (p_choice, com_choice) in [('r','s'), ('p','r'), ('s','p')]:
        print("🏆 Player wins!")
    else:
        print("🤖 Computer wins!")
