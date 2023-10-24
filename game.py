from piles.deck import Deck
from piles.discard import Discard
from players.player import Player


class Game:
    def __init__(self, player_count):
        self.deck, self.discard, self.players = self.setup(player_count)
        self.deck, self.players = self.deal(self.deck, self.players)
        self.current_player = 0
        self.direction = 1

        while True:
            print(f"\nPlayer {self.current_player + 1}'s turn")
            result = self.turn(self.players[self.current_player], self.discard, self.deck)
            if result == -1:
                break
            elif result == 1:
                print("Skipping next player's turn.")
                self.current_player += 1
            elif result == 2:
                print("Reversing direction of play.")
                self.direction *= -1
            elif result == 3:
                print("Next player draws 2!")
                next_player = (self.current_player + self.direction) % len(self.players)
                self.players[next_player].give(self.deck.draw_card())
                self.players[next_player].give(self.deck.draw_card())
                self.current_player += self.direction
            elif result == 4:
                print("Changing color to...")
                color = self.choose_color()
                self.discard.top_card.color = color
            elif result == 5:
                print("Next player draws 4!")
                next_player = (self.current_player + self.direction) % len(self.players)
                for _ in range(4):
                    self.players[next_player].give(self.deck.draw_card())
                self.current_player += self.direction
                print("Changing color to...")
                color = self.choose_color()
                self.discard.top_card.color = color

            self.current_player = (self.current_player + self.direction) % len(self.players)

        print(f"Player {self.current_player + 1} wins!")

    @staticmethod
    def setup(player_count):
        deck = Deck()
        discard = Discard()
        card = deck.draw_card()
        while card.action:
            deck.add_card(card)
            deck.shuffle()
            card = deck.draw_card()
        discard.add(card)
        players = [Player() for _ in range(player_count)]
        return deck, discard, players

    @staticmethod
    def deal(deck, players):
        for player in players:
            for _ in range(7):
                player.give(deck.draw_card())
        return deck, players

    @staticmethod
    def choose_color():
        color = input("Red, Blue, Green, or Yellow? ").title()
        while color not in ["Red", "Blue", "Green", "Yellow"]:
            print("Invalid color.")
            color = input("Red, Blue, Green, or Yellow? ").title()
        return color

    @staticmethod
    def turn(player, discard, deck):
        for card in player.hand:
            if card.is_playable(discard.top_card):
                break
        else:
            print("You have no playable cards. Drawing...")
            player.give(deck.draw_card())
            return 0
        print("Your hand: ")
        print(player.output(discard.top_card))
        print(f"\nTop card: {discard.top_card}")

        card_index = input("Which card would you like to play? ")
        while not (card_index.isnumeric() and player.play_card(int(card_index) - 1, discard)):
            print("That card is not playable.")
            card_index = input("Which card would you like to play? ")

        print(f"Playing card: {discard.top_card}")

        if len(player.hand) == 0:
            print("You win!")
            return -1
        elif len(player.hand) == 1:
            print("UNO!")
        elif action := discard.top_card.action:
            return {"skip": 1, "switch": 2, "plustwo": 3, "wild": 4, "four": 5}[action]
        return 0


if __name__ == '__main__':
    player_count = 2
    game = Game(player_count)
