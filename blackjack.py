SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

from card_oop import Card
from random import shuffle
import sys

deck = []

# Build the deck
for suit in SUITS:
	for rank in RANKS:
		card = Card(rank, suit)
		deck.append(card)

# Shuffle the deck and ready to play
shuffle(deck)

player_hand = []
dealer_hand = []

# Give cards to the player and the dealer
for _ in range(2):
	player_hand.append(deck.pop())
	dealer_hand.append(deck.pop())

def show_hand(who, hand):
	print("\n" + who + "\n")
	for card in hand:
		print(card.show_card_info())

# this function checks for a win due to a blackjack or a loss by busting
def check(who, hand):
	hand_sum = sum([card.bjvalue for card in hand])
	if hand_sum > 21:
		print(f"\n{who} busts and loses")
		sys.exit()
	else: # adjusting for an ace here
		for card in hand:
			if card.rank == "Ace":
				hand_sum += 10
				if hand_sum == 21 and len(hand) == 2:
					print(f"\n{who} wins by getting a blackjack")
					sys.exit()
				elif hand_sum > 21:
					hand_sum -= 10
	return hand_sum


print("\nAfter dealing")
show_hand("Player", player_hand)

print("\nDealer")
print(f"Has a hidden card and {dealer_hand[1].show_card_info()}")

player_sum = check("Player", player_hand)
dealer_sum = check("Dealer", dealer_hand)
print("Player has a hand value of", player_sum)

while True:
	opt = input("\nWould you like to hit or stand ? ") # asking player if they want to hit or stand
	if opt not in ['hit', 'stand']:
		continue
	if opt == 'hit':
		player_hand.append(deck.pop()) # Add the card
		show_hand("Player", player_hand) # show the complete hand
		# check for win after every card is added
		player_sum = check("Player", player_hand)
		dealer_sum = check("Dealer", dealer_hand)
		print("Player has a hand value of", player_sum)
	if opt == 'stand':
		break

while dealer_sum < 17: # the dealer takes a card until his hand exceeds 17
	dealer_hand.append(deck.pop())
	player_sum = check("Player", player_hand)
	dealer_sum = check("Dealer", dealer_hand)


show_hand("Player", player_hand)
show_hand("Dealer", dealer_hand)

print("Player has a hand value of", player_sum)
print("Dealer has a hand value of", dealer_sum)

# Compare hands and check winner
if player_sum > dealer_sum:
	print("\nPlayer wins")
elif player_sum < dealer_sum:
	print("\nDealer wins")
else:
	print("\nIt's a push, you tied")
