# Import random
from Cards import Deck
from player import Player


def main():
    print("Welcome to Two-Deck War!")

    # Create and shuffle two separate decks.
    deck1 = Deck()
    deck2 = Deck()
    deck1.shuffle()
    deck2.shuffle()

    # Give each player the cards from their own deck.
    player1 = Player("Player 1", deck1.cards)
    player2 = Player("Player 2", deck2.cards)

    print("Player 1 cards:", player1.count_cards())
    print("Player 2 cards:", player2.count_cards())
    
    round_number = 1

    # Keep playing while both players have cards.
    while player1.has_cards() and player2.has_cards():
        print(f"\nRound {round_number}:")

        # Collect the cards played this round, including any war cards.
        cards_in_round = []

        card1 = player1.draw_card()
        card2 = player2.draw_card()

        if card1 is None or card2 is None:
            break

        cards_in_round.extend([card1, card2])
        print(f"{player1.name} drew the {card1}.")
        print(f"{player2.name} drew the {card2}.")

        # Keep drawing while the cards tie.
        while card1.value == card2.value:
            print("War!")

            # If a player has no card left to draw, the other player wins the cards.
            if not player1.has_cards():
                player2.add_cards(cards_in_round)
                print(f"{player2.name} wins the war!")
                break
            if not player2.has_cards():
                player1.add_cards(cards_in_round)
                print(f"{player1.name} wins the war!")
                break

            card1 = player1.draw_card()
            card2 = player2.draw_card()
            cards_in_round.extend([card1, card2])
            print(f"{player1.name} drew the {card1}.")
            print(f"{player2.name} drew the {card2}.")
        else:
            # The cards were not equal.
            if card1.value > card2.value:
                player1.add_cards(cards_in_round)
                print(f"{player1.name} wins the round!")
            else:
                player2.add_cards(cards_in_round)
                print(f"{player2.name} wins the round!")

        print(f"{player1.name} has {player1.count_cards()} cards.")
        print(f"{player2.name} has {player2.count_cards()} cards.")
        round_number += 1

    # determine winner when one player has collected all the cards.
    if player1.has_cards():
        print(f"{player1.name} has collected all of the cards.")
        print(f"{player1.name} wins the game!")
    else:
        print(f"{player2.name} has collected all of the cards.")
        print(f"{player2.name} wins the game!")

#executes main
if __name__ == "__main__":
    main()
