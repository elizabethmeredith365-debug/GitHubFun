class Card:
	FACE_NAMES = {
		11: "Jack",
		12: "Queen",
		13: "King",
		14: "Ace",
	}

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __str__(self):
		card_value = Card.FACE_NAMES.get(self.value, str(self.value))
		return f"{card_value} of {self.suit}"

	def __gt__(self, other):
		return self.value > other.value

	def __eq__(self, other):
		return self.value == other.value


class Deck:
	SUITS = ["Spades", "Hearts", "Clubs", "Diamonds"]
	LOWEST_VALUE = 2
	HIGHEST_VALUE = 14

	def __init__(self):
		self.cards = []

		for suit in Deck.SUITS:
			for value in range(Deck.LOWEST_VALUE, Deck.HIGHEST_VALUE + 1):
				self.cards.append(Card(suit, value))