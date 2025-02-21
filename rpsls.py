import random


def main():
    print(generate_outcomes())

def generate_outcomes():

    outcomes = {}

    outcomes["scissors"] = ("paper", "lizard")
    outcomes["paper"] = ("rock", "spock")
    outcomes["rock"] = ("lizard")
    outcomes["lizard"] = ("spock", "paper")
    outcomes["spock"] = ("scissors", "rock") 

    return outcomes


if __name__ == "__main__":
    main()