from Classes import Card
from Classes import Hand


def starting_hand_input(hand_obj):
    while True:
        card1_input = input("Please enter your first starting card: ")
        if validate_input(card1_input, hand_obj) == True:
            card1 = Card(card1_input[0], card1_input[1])
            hand_obj.add_card(card1)
            print(f"You entered {card1}")
            break
        else:
            print("Invalid input, please try again.")

    while True:
        card2_input = input("Please enter your second starting card: ")
        if validate_input(card2_input, hand_obj) == True:
            card2 = Card(card2_input[0], card2_input[1])
            hand_obj.add_card(card2)
            print(f"You entered {card2}")
            break
        else:
            print("Invalid input, please try again.")


def flop_input(hand_obj):
    while True:
        flop2_input = input("Please enter the first flop card: ")
        if validate_input(flop2_input, hand_obj) == True:
            flop1 = Card(flop2_input[0], flop2_input[1])
            hand_obj.add_card(flop1)
            print(f"You entered {flop1}")
            break
        else:
            print("Invalid input, please try again.")

    while True:
        flop2_input = input("Please enter the second flop card: ")
        if validate_input(flop2_input, hand_obj) == True:
            flop2 = Card(flop2_input[0], flop2_input[1])
            hand_obj.add_card(flop2)
            print(f"You entered {flop2}")
            break
        else:
            print("Invalid input, please try again.")

    while True:
        flop3_input = input("Please enter the third flop card: ")
        if validate_input(flop3_input, hand_obj) == True:
            flop3 = Card(flop3_input[0], flop3_input[1])
            hand_obj.add_card(flop3)
            print(f"You entered {flop3}")
            break
        else:
            print("Invalid input, please try again.")


def validate_input(card, hand):
    card_rank = card[0]
    card_suit = card[1]

    if len(card) == 2:
        if card_rank.lower() not in ('2', '3', '4', '5', '6', '7', '8', '9', 't', 'j', 'q', 'k', 'a'):
            return False
        if card_suit.lower() not in ('h', 'd', 'c', 's'):
            return False
        for hand_card in hand.player_hand:
            if card[0] == hand_card.rank and card[1] == hand_card.suit:
                print("This card already exists in this hand")
                return False

        return True  # Only reached if rank, suit, uniqueness are all valid


def run_game():
    card_hand = Hand()
    print("         poker calculator")
    print("----------------------------------")
    starting_hand_input(card_hand)
    print(card_hand)
    flop_input(card_hand)
    print(card_hand)


if __name__ == "__main__":
    run_game()
