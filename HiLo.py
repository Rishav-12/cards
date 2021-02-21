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

# Shuffle the deck and ready to play
shuffle(deck)
points = 0
print("NOTE : Aces are High")

curr_card = deck.pop()

# Game Loop
while len(deck) > 0:
	print("Current card is", curr_card.show_card_info())
	response = input("[H]igh or [L]ow ")

	# Check for an invalid response
	if response.lower() not in ['h', 'l']:
		print("Please enter valid option...")
		continue

	next_card = deck.pop()
	print("Next card drawn :", next_card.show_card_info())

	# Now make the required comparisons
	if next_card.value > curr_card.value:
		if response.lower() == 'h':
			print("\nYou guessed correctly. You get a point\n")
			points += 1
			print("Score", points)
		else:
			print("\nIncorrect guess\n")
			break
	elif next_card.value < curr_card.value:
		if response.lower() == 'l':
			print("\nYou guessed correctly. You get a point\n")
			points += 1
			print("Score", points)
		else:
			print("\nIncorrect guess\n")
			break
	else:
		print("\nThe next card is neither lower nor higher. Keep Playing\n")
		print("Score", points)

	curr_card = next_card # The 'next_card' in the last round is now the 'curr_card'

if len(deck) == 0:
	print("You have run out of cards. You are a champion since you guessed all the cards correctly.")
print(f"Game Over.\nFinal score : {points} points")
