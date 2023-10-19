import random
from cards.card import Card
from cards.special_card import SpecialCard

class Deck:
    def __init__(self):
        self.cards = []
        self.setup_deck()

    def setup_deck(self):
        colors = ['Red', 'Blue', 'Green', 'Yellow']
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        special_cards = [('Skip', 'Skip Next Player'), ('Reverse', 'Reverse Direction of Play'), ('Draw Two', 'Draw Two Cards and Forfeit Turn')]

        for color in colors:
            self.cards.append(Card(color, '0'))
            for value in values:
                for _ in range(2):
                    self.cards.append(Card(color, value))
            for special in special_cards:
                for _ in range(2):
                    self.cards.append(SpecialCard(color, special[0], special[1]))

        for _ in range(4):
            self.cards.append(SpecialCard('Wild', 'Wild', 'Change Color'))
            self.cards.append(SpecialCard('Wild', 'Wild Draw Four', 'Change Color and Draw Four Cards'))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            raise IndexError("The deck is empty.")

    def add_card(self, card):
        self.cards.append(card)

    # Other deck management methods go here
