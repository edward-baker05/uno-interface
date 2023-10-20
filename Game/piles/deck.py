import random
from piles.discard import Discard
from cards.card import Card
from cards.special_card import SpecialCard

class Deck:
    def __init__(self):
        self.cards = []
        self.setup_deck()
        
    def __str__(self):
        return f"Deck: {self.cards}"

    def setup_deck(self):
        """
        Sets up the deck with the standard 108 cards.
        """
        colors = ['Red', 'Blue', 'Green', 'Yellow']
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        special_cards = ['skip', 'switch', 'two']

        for color in colors:
            self.cards.append(Card(color, '0'))
            for value in values:
                for _ in range(2):
                    self.cards.append(Card(color, value))
            for i, special in enumerate(special_cards):
                for _ in range(2):
                    self.cards.append(SpecialCard(color, -(i+1), special))

        for _ in range(4):
            self.cards.append(SpecialCard('wild', 4, 'wild'))
            self.cards.append(SpecialCard('wild', 5, 'four'))

        self.shuffle()

    def shuffle(self):
        """
        Shuffles the deck.
        """
        random.shuffle(self.cards)

    def draw_card(self, discard: Discard=[]) -> Card:
        """
        Draws a card from the deck.
        
        Parameters:
            discard (Discard): The discard pile
        
        Returns:
            Card: The card drawn
        """
        if not self.cards:
            self.cards = discard.cards[::-1]
            discard.cards = []
        return self.cards.pop()            

    def add_card(self, card): # No idea why this exists
        """
        Adds a card to the deck.
        
        Parameters:
            card (Card): The card to add
        """
        self.cards.append(card)

