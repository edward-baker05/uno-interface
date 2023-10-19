class Card:
    def __init__(self, color: str, value: int):
        """
        Parameters:
        color (str): The color of the card
        value (int): The value of the card
        """
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.color} {self.value}"

    def is_playable(self, top_card):
        return self.color == top_card.color or self.value == top_card.value
        