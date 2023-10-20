from piles.deck import Deck
from piles.discard import Discard
from player import Player


def setup() -> tuple:
    """
    The setup function creates the deck, discard pile, and players.

    Returns:
        deck (Deck): The deck
        discard (Discard): The discard pile
        players (list): The list of players
    """
    deck = Deck()
    discard = Discard()
    card = deck.draw_card()
    while card.action:
        deck.add_card(card)
        deck.shuffle()
        card = deck.draw_card()
    discard.add(card)
    player_count = 4
    players = [Player() for _ in range(player_count)]
    return deck, discard, players


def deal(deck: Deck, players: list) -> tuple:
    """
    Deals 7 cards to each player.

    Parameters:
        deck (Deck): The deck
        players (list): The list of players

    Returns:
        deck (Deck): The deck
        players (list): The list of players
    """
    for player in players:
        for _ in range(7):
            player.give(deck.draw_card())
    print(players)
    return deck, players


def turn(player: Player, discard: Discard, deck: Deck) -> int:
    """
    Handles the logic for a player's turn.

    Parameters:
        player (Player): The player whose turn it is
        discard (Discard): The discard pile
        deck (Deck): The deck

    Returns:
        bool: The outcome of the players turn
    """
    for card in player.hand:
        if card.is_playable(discard.top_card):
            break
    else:
        print("You have no playable cards. Drawing...")
        player.give(deck.draw_card())
        return 0
    print("Your hand: ")
    print(player)
    print(f"\nTop card: {discard.top_card}")

    card = int(input("Which card would you like to play? ")) - 1
    while not player.play_card(card, discard):
        print("That card is not playable.")
        card = int(input("Which card would you like to play? ")) - 1

    print(f"Playing card: {discard.top_card}")
    
    if len(player.hand) == 0:
        print("You win!")
        return -1
    elif len(player.hand) == 1:
        print("UNO!")
    elif action := discard.top_card.action:
        return {"skip": 1, "switch": 2, "two": 3, "wild": 4, "four": 5}[action]
    return 0


def main():
    """
    The main logic for running the game.
    """
    deck, discard, players = setup()
    deck, players = deal(deck, players)
    current_player = 0
    direction = 1

    while True:
        print(f"\nPlayer {current_player+1}'s turn")
        result = turn(players[current_player], discard, deck)
        print(f"{result}======")
        match result:
            case -1:
                break
            case 1:
                print("Skipping next player's turn.")
                current_player += 1
            case 2:
                print("Reversing direction of play.")
                direction *= -1
            case 3:
                print("Next player draws 2!")
                players[(current_player + 1) % len(players)].give(deck.draw_card())
                players[(current_player + 1) % len(players)].give(deck.draw_card())
                current_player += 1
            case 4:
                print("Changing color to...")
                color = input("Red, Blue, Green, or Yellow? ").title()
                while color not in ["Red", "Blue", "Green", "Yellow"]:
                    print("Invalid color.")
                    color = input("Red, Blue, Green, or Yellow? ").title()
                discard.top_card.color = color
            case 5:
                print("Next player draws 4!")
                players[(current_player + 1) % len(players)].give(deck.draw_card())
                players[(current_player + 1) % len(players)].give(deck.draw_card())
                players[(current_player + 1) % len(players)].give(deck.draw_card())
                players[(current_player + 1) % len(players)].give(deck.draw_card())
                current_player += 1
                print("Changing color to...")
                color = input("Red, Blue, Green, or Yellow? ").title()
                while color not in ["Red", "Blue", "Green", "Yellow"]:
                    print("Invalid color.")
                    color = input("Red, Blue, Green, or Yellow? ").title()
                discard.top_card.color = color

        current_player = (current_player + 1) % len(players)

    print(f"Player {current_player+1} wins!")


main()
