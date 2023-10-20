class Discard:
    def __init__(self):
        self.cards = []
        self.top_card = None
        
    def add(self, card):
        self.cards.append(card)
        self.top_card = card
        
    def get_discard(self):
        return self.cards