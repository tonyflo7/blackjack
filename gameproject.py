# This game is created with the intention of helping Python beginners.
# Game of Blackjack (objective of the player is to have a sum of 21 or less)

import random

# Ask if the player wants to play Blackjack to begin.
playtime = input("Ready to play some Blackjack? 'yes' or 'no': ").lower()

while True:
    if playtime == 'yes':
        print("Let's jiggy.\n")
    elif playtime == 'no':
        print("Sounds like you're not ready.")
        print("Maybe next time.")
        break


    # Set up the deck of cards
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


    # Playing logic
    while True:
        player_score = sum(card_value(card) for card in player_card)
        dealer_score = sum(card_value(card) for card in dealer_card)
        print("Cards player has:", player_card)
        print("Score of the player:", player_score)
        print("\n")
        choice = input("What do you want? ['play' to request another card or 'stop' to stop?]: ").lower()

        # Decision to play
        if choice == 'play':
            new_card = deck.pop()
            player_card.append(new_card)
        elif choice == 'stop':
            break
        else:
            print('Invalid input. Please try again.')
            continue

        # Logic if dealer beats the player
        if player_score > 21:
            print("Cards the dealer has:", dealer_card)
            print("Score of the dealer:", dealer_score)
            print("Cards the player has:", player_card)
            print("Score of the player:", player_score)
            print("Dealer wins. The player because exceeded a score of 21.")

        # Logic for dealer to keep drawing card until score is at least 17
        while dealer_score < 17:
            new_card = deck.pop()
            dealer_card.append(new_card)
            dealer_score += card_value(new_card)

        print("Cards the dealer has:", dealer_card)
        print("Score the dealer has:", dealer_score)
        print("\n")


    # Determining the winner with all outcomes
    if dealer_score > 21:
        print("Cards dealer has:", dealer_card)
        print("Dealer score is:", dealer_score)
        print("Cards player has:", player_card)
        print("Player score is:", player_score)
        print("Player wins. Dealer loses because score exceeds 21.")
    elif player_score > 21:
        print("Cards dealer has:", dealer_card)
        print("Dealer score is:", dealer_score)
        print("Cards player has:", player_card)
        print("Player score is:", player_score)
        print("Dealer wins. Player loses because score exceeds 21.")
    elif player_score > dealer_score and player_score < 21:
        print("Cards dealer has:", dealer_card)
        print("Dealer score is:", dealer_score)
        print("Cards player has:", player_card)
        print("Player score is:", player_score)
        print("Player wins. Player had higher score than dealer under 21.")
    elif dealer_score > player_score and dealer_score < 21:
        print("Cards dealer has:", dealer_card)
        print("Dealer score is:", dealer_score)
        print("Cards player has:", player_card)
        print("Player score is:", player_score)
        print("Dealer wins. Dealer has higher score than player under 21.")
    elif player_score == 21:
        print("Cards dealer has:", dealer_card)
        print("Dealer score is:", dealer_score)
        print("Cards player has:", player_card)
        print("Player score is:", player_score)
        print("Player wins. Player score equals 21.")
    elif dealer_score == 21:
        print("Cards dealer has:", dealer_card)
        print("Dealer score is:", dealer_score)
        print("Cards player has:", player_card)
        print("Player score is:", player_score)
        print("Dealer wins. Dealer score equals 21.")
    else:
        print("Cards dealer has:", dealer_card)
        print("Dealer score is:", dealer_score)
        print("Cards player has:", player_card)
        print("Player score is:", player_score)
        print("It's a tie.")
    break