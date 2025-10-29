import random

CHOICES = ["rock", "paper", "scissors"]


def get_computer_choice():
    return random.choice(CHOICES)


def normalize(choice):
    return choice.lower().strip()

def determine_winner(player, computer):
    player = normalize(player)
    computer = normalize(computer)

    if player not in CHOICES or computer not in CHOICES:
        return "invalid"

    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"
    
if __name__ == "__main__":
    player = input("Choisis rock, paper ou scissors : ")
    computer = get_computer_choice()
    result = determine_winner(player, computer)

    print(f"Tu as choisi : {player}")
    print(f"L'ordinateur a choisi : {computer}")
    print(f"Résultat : {result}")
