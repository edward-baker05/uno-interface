from cards.card import Card

class SpecialCard(Card):
    def __init__(self, color: str, value: str, action: str):
        """
        Parameters:
        color (str): The color of the card
        value (str): The value of the card
        action (str): The action of the card
        """
        super().__init__(color, value)
        self.action = action

    def __str__(self):
        return f"{self.color} {self.action}"