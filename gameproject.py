# This game is created with the intention of getting experience for a better job.

import random

card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(card, category) for category in card_categories for card in cards_list]


# This function takes the card inputs and returns the corresponding value
def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])
    

# Shuffle the deck of cards
random.shuffle(deck)
# Draw a card to the player and to the dealer
player_card = [deck.pop(), deck.pop()]
dealer_card = [deck.pop(), deck.pop()]


# print(input('Ready to play some Blackjack? Yes or no: '))