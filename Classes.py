class Card:
    SUIT = ('h', 'd', 'c', 's')
    RANK = ('2', '3', '4', '5', '6', '7', '8', '9', 't', 'j', 'q', 'k', 'a')

    def __init__(self, rank, suit):
        if rank not in self.RANK:
            raise ValueError("Invalid rank")
        if suit not in self.SUIT:
            raise ValueError("Invalid suit")
        self.rank = rank
        self.suit = suit


    def __str__(self):
        rank_name = {'1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine', 't':'Ten', 'j':'Jack', 'q':'Queen', 'k':'King', 'a':'Ace'}
        suit_name = {"h": "Hearts", "d": "Diamonds", "s": "Spades", "c": "Clubs"}
        return f"{rank_name[self.rank]} of {suit_name[self.suit]}"


class Hand:

    def __init__(self):
        self.player_hand = []

    def add_card(self, card):
        self.player_hand.append(card)

    def evaluate_hand(self):
        print("parp")


    def __str__(self):
        result = "\nYour hand consists of:\n"
        for card in self.player_hand:
            result += f"- {card}\n"
        return result