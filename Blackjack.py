"""This program plays a single-player game of blackjack"""
from random import randint
from collections import Counter

class Cards:
    def __init__(self, suit, value, score):
        self.suit = suit
        self.value = value
        self.score = score

    def __repr__(self):
        return "{value} {suit}".format(suit = self.suit, value = self.value)

deck =[]

def make_deck():
    global deck
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    values = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
    #"K", "Q", "J", 10, 9, 8, 7, 6, 5,
    scores = {"A": 11, "K": 10, "Q": 10, "J": 10, 10: 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2}
    
    for suit in suits:
        for value in values:
            deck.append(Cards(suit, value, scores[value]))

def keep_playing():
    if bank <= 0:
        print("Game Over. You lost all of your money.")
        quit()
    play_again = input("Play again? Y for Yes or N for No: ")
    if play_again.upper() == "Y":
        deal()
    elif play_again.upper() != "Y" and play_again.upper() != "N":
        print("Invalid entry.")
        keep_playing()
    else:
        quit()

print("Welcome to Blackjack.  Enjoy the game.")

player = input("Enter name: ")  
bank = float(input("Enter starting money ammount: $"))

def deal():
    make_deck()
    player_hand = []
    player_score = 0
    dealer_hand = []
    dealer_score = 0
    global bank
    global deck
    while True:
        wager = float(input("Place your bet: $"))
        if wager > bank:
            print("Can not wager more than you have. Player Bank has $" + str(bank))
            continue
        else:
            bank -= wager
            break

    # Deal and display player_hand and player_score.
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
        
        print("Player Hand: " + str(player_hand))
        print("Player has " + str(player_score))
        
        if player_score == 21:
            bank += wager + wager * 3 / 2
            print("Blackjack!!! Player wins.")
            print("Player Bank: $ " + str(bank))
            keep_playing()
            return
    
    # Deal dealer_hand. Display only the first card of the hand.
    while len(dealer_hand) < 2:
        dealer_card_1 = deck[randint(0, len(deck) - 1)]
        #dealer_card_1 = deck[0]
        dealer_hand.append(dealer_card_1)
        dealer_score += dealer_card_1.score
        deck.remove(dealer_card_1)

        print("Dealer Hand: " + str(dealer_hand))
        print("Dealer has " + str(dealer_score))
    
        dealer_card_2 = deck[randint(0, len(deck) - 1)]
        dealer_hand.append(dealer_card_2)
        if dealer_card_1.score == 11 and dealer_card_2.score == 11:
            dealer_card_2.score = 1
            dealer_score += dealer_card_2.score
        else:    
            dealer_score += dealer_card_2.score
        deck.remove(dealer_card_2)

    # Logic for player to Hit or Stand.
    while player_score < 21:
        play = input("Choose your play. Press 'H' for Hit or 'S' for Stand. You choose to :")
        if play.upper() == "H":
            player_card_3 = deck[randint(0, len(deck) - 1)]
            player_hand.append(player_card_3)
            player_score += player_card_3.score
            deck.remove(player_card_3)
            
            #Accounts for Aces in player_hand.  Aces can be worth 11 or 1.
            for i in player_hand:
                while player_score > 21 and i.score == 11:
                    i.score == 1
                    player_score -= 10
                    return player_score
                
                
                if player_score > 21:
                    print("Player Hand: " + str(player_hand))
                    print("Player has " + str(player_score))
                    print("Player Busts.")
                    print("Player Bank: $" + str(bank))
                    keep_playing()
                    return
            print("Player Hand: " + str(player_hand))
            print("Player has " + str(player_score))
            
        
        elif play.upper() == "S":
            print("Player stands at " + str(player_score))
            break

    #Dealer hand logic. Dealer stands on hard 17 and over. Dealer hits on soft 17 and under.
    print("Dealer Hand: " + str(dealer_hand))
    print("Dealer has " + str(dealer_score))
    while dealer_score <= 16:
        dealer_card_3 = deck[randint(0, len(deck) - 1)]
        dealer_hand.append(dealer_card_3)
        dealer_score += dealer_card_3.score
        deck.remove(dealer_card_3)
        for i in dealer_hand:
            while dealer_score > 21 and i.score == 11:
                i.score == 1
                dealer_score -= 10
        print("Dealer Hand: " + str(dealer_hand))
        print("Dealer has " + str(dealer_score))

        #Dealer bust
        if dealer_score > 21:
            bank += wager * 2
            print("Dealer Busts!. Player wins.")
            print("Player Bank : $" + str(bank))
            keep_playing()
            return

    # Dealer with Ace in hand
    for i in dealer_hand:
        while dealer_score == 17 and i.score == 11:
            dealer_card_3 = deck[randint(0, len(deck) - 1)]
            dealer_hand.append(dealer_card_3)
            dealer_score += dealer_card_3.score
            deck.remove(dealer_card_3)
            if dealer_score > 21:
                i.score == 1
                dealer_score -= 10
                break

            print("Dealer Hand: " + str(dealer_hand))
            print("Dealer has " + str(dealer_score))
    
    # Compare results and pay out winnings.
    if player_score > dealer_score and dealer_score <= 21:
        bank += wager * 2
        print("Player Wins!")
        print("Player Bank: $" + str(bank))

    elif dealer_score > player_score:
        print("Dealer wins.")
        print("Player Bank: $" + str(bank))

    else: 
        bank += wager
        print("Its a Tie.")
        print("Player Bank: $" + str(bank))

    

    keep_playing()
    
deal()
