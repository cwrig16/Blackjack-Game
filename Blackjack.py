"""This program plays a single-player game of blackjack"""
from random import randint

class Cards:
    def __init__(self, suit, value, score):
        self.suit = suit
        self.value = value
        self.score = score

    def __repr__(self):
        return "{value} {suit}".format(suit = self.suit, value = self.value)

suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
values = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
scores = {"A": 11, "K": 10, "Q": 10, "J": 10, 10: 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2}
deck =[]
for suit in suits:
    for value in values:
        deck.append(Cards(suit, value, scores[value]))

#print("Welcome to Blackjack.  Enjoy the game.")

# player = input("Enter name: ")    
bank = int(input("Enter starting money ammount: $"))
while True:
    wager = int(input("Place your bet: $"))
    if wager > bank:
        print("Can not wager more than you have. Player Bank has $" + str(bank))
        continue
    else:
        bank -= wager
        break

# print("Dealing Cards...")

def deal():
    player_hand = []
    player_score = 0
    dealer_hand = []
    dealer_score = 0
    if len(player_hand) < 2:
        player_card_1 = deck[randint(0, len(deck) - 1)]
        player_hand.append(player_card_1)
        player_score += player_card_1.score
        deck.remove(player_card_1)
        
        player_card_2 = deck[randint(0, len(deck) - 1)]
        player_hand.append(player_card_2)
        if player_card_1.score == 11 and player_card_2.score == 11:
            player_card_2.score = 1
            player_score += player_card_2.score
        else:    
            player_score += player_card_2.score
        deck.remove(player_card_2)
        
        print(player_hand)
        print("Player has " + str(player_score))
        
        if player_score == 21:
            global bank
            bank += wager + wager * 3 / 2
            print("Blackjack!!! Player wins.")
            print("Player Bank: $ " + str(bank))

    while len(dealer_hand) < 2:
        dealer_card_1 = deck[randint(0, len(deck) - 1)]
        dealer_hand.append(dealer_card_1)
        dealer_score += dealer_card_1.score
        deck.remove(dealer_card_1)

        print(dealer_hand)
        print("Dealer has " + str(dealer_score))
    
        dealer_card_2 = deck[randint(0, len(deck) - 1)]
        dealer_hand.append(dealer_card_2)
        if dealer_card_1.score == 11 and dealer_card_2.score == 11:
            dealer_card_2.score = 1
            dealer_score += dealer_card_2.score
        else:    
            dealer_score += dealer_card_2.score
        deck.remove(dealer_card_2)

    while player_score < 21:
        play = input("Choose your play. Press 'H' for Hit or 'S' for Stand. You choose to :")
        if play.upper() == "H":
            player_card_3 = deck[randint(0, len(deck) - 1)]
            player_hand.append(player_card_3)
            player_score += player_card_3.score
            deck.remove(player_card_3)
            
            print(player_hand)
            print("Player has " + str(player_score))
            
        
        elif play.upper() == "S":
            print("Player stands at " + str(player_score))
            break
deal()
