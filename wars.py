SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

from card_oop import Card
from random import shuffle

deck = []

# Build the deck
for suit in SUITS:
	for rank in RANKS:
		card = Card(rank, suit)
		deck.append(card)

shuffle(deck)

# Deal out the cards to the players
player_1 = deck[0:26]
player_2 = deck[26:52]

# Utility Function to add cards to a player's hand
def add_card_to_hand(hand, card):
	hand.insert(0, card)

print("Current Status")
print("Player 1", len(player_1))
print("Player 2", len(player_2))

while len(player_1) != 0 and len(player_2) != 0:
	# Players flip over a card
	player_1_card = player_1.pop()
	player_2_card = player_2.pop()
	print("Player 1", player_1_card.show_card_info())
	print("Player 2", player_2_card.show_card_info())

	# The cards are compared and appropriate actions are taken
	if player_1_card.value > player_2_card.value:
		print("Player 1 takes the hand")
		add_card_to_hand(player_1, player_2_card)
		add_card_to_hand(player_1, player_1_card)
	elif player_1_card.value < player_2_card.value:
		print("Player 2 takes the hand")
		add_card_to_hand(player_2, player_1_card)
		add_card_to_hand(player_2, player_2_card)

	# Show the current number of cards with each player
	print("Current Status")
	print("Player 1", len(player_1))
	print("Player 2", len(player_2))

print("Well played both players. All the best for your next game.")
# IMPORTANT: I have not yet implemented the "War" situation