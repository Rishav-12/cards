VALUES = {'Ace' : 14, 'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5, 'Six' : 6, 'Seven' : 7, 'Eight' : 8, 'Nine' : 9, 'Ten' : 10, 'Jack' : 11, 'Queen' : 12, 'King' : 13}

class Card():
	"""Initializes a Card object with a rank, a suit and a value"""
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		self.value = VALUES[self.rank]

	# Function shows information about the Card object
	def show_card_info(self):
		return (f"{self.rank} of {self.suit}")

	# Function checks if two cards have the same rank
	def same_rank(self, another_card):
		if self.rank == another_card.rank:
			return True
		return False

	# Function checks if two cards have the same suit
	def same_suit(self, another_card):
		if self.suit == another_card.suit:
			return True
		return False
