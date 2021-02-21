"""
NOTES: Aces are high
The game is now fully functional with war situation implemented
"""
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

# Function which handles a war situation
"""We put all the cards in a list and compare the appropriate ones"""
def war(check1, check2):
	for i in range(2):
		"""try-except block to handle error
		if someone runs out of cards during a war, he/she immediately loses"""
		try:
			war_cards.append(player_1.pop())
			war_cards.append(player_2.pop())
		except Exception as e:
			print("Someone has run out of cards")
			return False
	
	# Show one card face up, the other remains face down
	print(f"Player 1 turns over {war_cards[check1].show_card_info()}, and [hidden]")
	print(f"Player 2 turns over {war_cards[check2].show_card_info()}, and [hidden]")

	# Check which of the face up cards are higher, put all cards in the winner's hand
	if war_cards[check1].value > war_cards[check2].value:
		print("Player 1 wins the War")
		for card in war_cards:
			add_card_to_hand(player_1, card)
	elif war_cards[check1].value < war_cards[check2].value:
		print("Player 2 wins the War")
		for card in war_cards:
			add_card_to_hand(player_2, card)
	# If face up cards are again equal in rank, another round of war follows
	else:
		war(check1 + 4, check2 + 4)

print("Current Status")
print("Player 1", len(player_1))
print("Player 2", len(player_2))

war_cards = [] # This list contains all the cards dealt out during a war

while len(player_1) != 0 and len(player_2) != 0:
	war_cards = []
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
	else:
		"""If war situation arises,
		add the cards to a list and call the war() function"""
		war_cards.append(player_1_card)
		war_cards.append(player_2_card)
		print("It's time for War!")
		run = war(2, 3)
		# If war() returns False, someone has run out of cards
		if run == False:
			break

	# Show the current number of cards with each player
	print("Current Status")
	print("Player 1", len(player_1))
	print("Player 2", len(player_2))

print("Final Scores")
print("Player 1", len(player_1))
print("Player 2", len(player_2))
print("Well played both players. All the best for your next game.")
