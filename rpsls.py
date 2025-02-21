import random
import argparse

def main():

    parser = argparse.ArgumentParser(description="Rock, Paper, Scissors, Lizard, Spock game")
    parser.add_argument("rules", help="Rules of the game!")
    args = parser.parse_args()
    rules = args.rules

    outcome = generate_outcomes()

    player_name = get_player_name()
    print(f"{player_name}, welcome to a game of Rock, Paper, Scissors, Lizard, Spock")
    print()
    print(game_rules(rules))
    print()
    
    options = ["rock", "paper", "scissors", "lizard", "spock"]

    tries = 5
    rounds = 1
    computer_points = 0
    player_points = 0

    while tries > 0:

        print(f"Round {rounds} \nRock, Paper, Scissors, Lizard, Spock")

        player = player_moves()
        while player not in options:
            print("Invalid option, try again!")
            player = player_moves()

        computer = computer_moves(options)
        
        if player_win(computer, player, outcome):
            print(f"You chose {player}, computer chose {computer}, \nYou won this round")
            player_points += 1

        if computer_win(computer, player, outcome):
            print(f"Computer chose {computer} \nYou chose chose {player} \nComputer won this around")
            computer_points += 1

        if tie(computer, player):
            print(f"You and the computer both chose {computer} \nIt's a TIE! \nGo again!")

        tries -= 1
        rounds += 1

    print(f"After {rounds} rounds....")
    if computer_points > player_points:
        print(f"Computer won the game! \nComputer scored {computer_points} points! \nTry again!")
    elif computer_points == player_points:
        print(f"You and the computer got the same number of points, {computer_points} points. Its a tie!")
    else:
        print(f"Congratulations {player_name}. \nYou won the game!, scoring {player_points} points!")
        print("GET IN THERE CHAMP!")


def generate_outcomes():

    outcomes = {}

    outcomes["scissors"] = ("paper", "lizard")
    outcomes["paper"] = ("rock", "spock")
    outcomes["rock"] = ("lizard", "scissors")
    outcomes["lizard"] = ("spock", "paper")
    outcomes["spock"] = ("scissors", "rock") 

    return outcomes
        
def computer_win(computer, player, outcomes):

    for play in outcomes.keys():
        if computer == play and player in outcomes[play]:
            return True
        
    return False
        
def player_win(computer, player, outcomes):

    for play in outcomes.keys():

        if player == play and computer in outcomes[play]:
        
            return True
        
    return False
        
def tie(computer, player):

    if computer == player:

        return True
    
    return False

def computer_moves(options):

    return random.choices(options)[0]

def player_moves():

    return input("Choose a move to make Rock/Paper/Scissors/Lizard/Spock: ").lower().strip()

def get_player_name():

    return input("Enter your name: ").capitalize().strip()

def game_rules(filepath):

    try:
        with open(filepath, "r", newline="") as rules:
            reader = rules.read()

            return reader

            # return [line for line in rules]
    
    except FileNotFoundError:

        return "File not found"

if __name__ == "__main__":
    main()