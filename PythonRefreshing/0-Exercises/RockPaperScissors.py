import random

options = ("rock", "paper", "scissors")
playing = True

computer_wins = 0
player_wins = 0

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Rock, Paper or Scissors?: ").lower()

    print()
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
        player_wins += 1
    elif player == "paper" and computer == "rock":
        print("You win!")
        player_wins += 1
    elif player == "scissors" and computer == "paper":
        print("You win!")
        player_wins += 1
    else:
        print("You lose!")
        computer_wins += 1

    print()
    playing = input("Play again? (y/n): ").lower() == "y"
    

print()
print(f"Player wins: {player_wins}")
print(f"Computer wins: {computer_wins}")
print()