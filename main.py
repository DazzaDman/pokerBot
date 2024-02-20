from Card import Card


def starting_hand_input():

    while True:
        card1_input = input("Please enter your first starting card: ")
        if validate_input(card1_input) == True:
            card1 = Card(card1_input[0], card1_input[1])
            print(f"You entered {card1}")
            break
        else:
            print("Invalid input, please try again.")

    while True:
        card2_input = input("Please enter your second starting card: ")
        if validate_input(card2_input) == True:
            card2 = Card(card2_input[0], card2_input[1])
            print(f"You entered {card2}")
            break
        else:
            print("Invalid input, please try again.")

def flop_input():
    print("fart")


def validate_input(card):
    card_rank = card[0]
    card_suit = card[1]

    if len(card) == 2:
        if card_rank.lower() not in ('2', '3', '4', '5', '6', '7', '8', '9', 't', 'j', 'q', 'k', 'a'):
            return False
        if card_suit.lower() not in ('h', 'd', 'c', 's'):
            return False
        return True  # Only reached if both rank and suit are valid


def run_game():
    print("         poker calculator")
    print("----------------------------------")
    starting_hand_input()
    print()

run_game()

