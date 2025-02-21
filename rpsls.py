import random


def main():
    print(generate_outcomes())

    outcome = generate_outcomes()
    player = "rock"
    computer = "scissors"

    print(determine_winner(computer, player, outcome))

def generate_outcomes():

    outcomes = {}

    outcomes["scissors"] = ("paper", "lizard")
    outcomes["paper"] = ("rock", "spock")
    outcomes["rock"] = ("lizard", "scissors")
    outcomes["lizard"] = ("spock", "paper")
    outcomes["spock"] = ("scissors", "rock") 

    return outcomes

def determine_winner(computer, player, outcomes):

    if computer == player:

        return f"You and the computer both played {computer} \nIt is a tie \nGo again!"

    for play in outcomes.keys():
        if computer == play and player in outcomes[play]:
            return f"Computer chose {computer} \nYou chose chose {player} \nComputer won this around"
        
        if player == play and computer in outcomes[play]:
            return f"You chose {player}, computer chose {computer}, \nYou won this round"
        


if __name__ == "__main__":
    main()