import random

options = ("rock", "paper", "scissor")
playing = True

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissor): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissor":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player=="scissor" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

        play_again=("Play again? (y/n): ").lower()
        if not play_again== ("y", "yes"):

            playing = False

print("Thanks for playing!")