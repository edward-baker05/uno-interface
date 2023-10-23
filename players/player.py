from piles.discard import Discard

class Player:
    def __init__(self):
        """
        Parameters:
            hand (list): The player's hand
        """
        self.hand = []
    
    def __str__(self):
        output = ""
        for i, card in enumerate(self.hand):
            output += f"{i+1}. {card}\n"
        return output
    
    def give(self, card):
        """
        Gives the player a card.
        
        Parameters:
            card (Card): The card to give to the player
        """
        self.hand.append(card)
    
    def set_hand(self, hand: list):
        """
        Sets the player's hand to the given list.
        
        Parameters:
            hand (list): The player's hand
        """
        self.hand = hand
    
    def draw_card(self, deck):
        """
        Draws a card from the deck and appends it to the player's hand.
        
        Parameters:
            deck (Deck): The deck to draw from
        """
        self.hand.append(deck.draw_card())
        
    def play_card(self, card: int, discard: Discard) -> bool:
        """
        Checks if a card is playable and handles the logic for playing a card.
        
        Parameters:
            card (int): The index of the card to play
            discard (Discard): The discard pile
            
        Returns:
            bool: Whether the card was playable
        """
        if self.hand[card].is_playable(discard.top_card):
            discard.add(self.hand[card])
            self.hand.remove(self.hand[card])
            return True
        return False