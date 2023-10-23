class Card:
    def __init__(self, color: str, value: int):
        """
        Parameters:
            color (str): The color of the card
            value (int): The value of the card
        """
        self.color = color
        self.value = value
        self.action = None

    def __str__(self):
        return f"{self.color} {self.value}"

    def is_playable(self, top_card) -> bool:
        """
        Checks if a card is playable.
        
        Parameters:
            top_card (Card): The top card of the discard pile
            
        Returns:
            bool: Whether the card is playable
        """
        return self.color == top_card.color or self.value == top_card.value or self.color == 'wild'
        