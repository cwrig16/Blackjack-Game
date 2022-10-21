"""This program plays a single-player game of blackjack"""
from random import randint
from collections import Counter
from re import S
from tkinter import Y

class Cards:
    def __init__(self, suit, value, score):
        self.suit = suit
        self.value = value
        self.score = score

    def __repr__(self):
        return "{value}{suit}".format(suit = self.suit, value = self.value)

deck =[]

def make_deck():
    global deck
    suits = ['\u2663', '\u2664', '\u2665', '\u2666']
    values = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
    #"A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2
    scores = {"A": 1, "K": 10, "Q": 10, "J": 10, 10: 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2}
    
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

#print("Welcome to Blackjack.  Enjoy the game.")

#player = input("Enter name: ")  
bank = float(input("Enter starting money ammount: $"))

def deal():
    make_deck()
    global bank
    global deck
    while True:
        player_hand = []
        dealer_hand = []
        wager = float(input("Place your bet: $"))
        if wager > bank:
            print(f"Can not wager more than you have. Player Bank has ${bank}")
            continue
        else:
            bank -= wager
            #break
        
    # Deal and display player_hand and player_score.
        while len(player_hand) < 2:
            player_hand.append(deck[randint(0, len(deck) - 1)])
            deck.remove(player_hand[-1])
            player_score = 0
            player_aces = 0
            for card in player_hand:
                if isinstance(card.value, int):
                    player_score += card.value
                else:
                    if card.value == "A":
                        player_aces += 1
                    else:
                        player_score += 10
            if player_aces == 1:
                if player_score < 11:
                    player_score += 11
                else:
                    player_score += 1
            if player_aces == 2:
                if player_score < 10:
                    player_score += 12
                else:
                    player_score += 2
            if player_aces == 3:
                if player_score < 9:
                    player_score += 13
                else:
                    player_score += 3
            if player_aces == 4:
                if player_score < 8:
                    player_score += 14
                else:
                    player_score += 4

            print(f"Player Hand: {player_hand}", end="")  
            print(f"   Player has {player_score}")          
        
            if player_score == 21:
                bank += wager + wager * 3 / 2
                print("Blackjack!!! Player wins.")
                print(f"Player Bank: ${bank}")
                keep_playing()
                break
        
        # Deal dealer_hand. Display only the first card of the hand.
        while len(dealer_hand) < 2:
            dealer_hand.append(deck[randint(0, len(deck) - 1)])
            deck.remove(dealer_hand[-1])
            dealer_score = 0
            dealer_aces = 0
            for card in dealer_hand:
                if isinstance(card.value, int):
                    dealer_score += card.value
                else:
                    if card.value == "A":
                        dealer_aces += 1
                    else:
                        dealer_score += 10
            if dealer_aces == 1:
                if dealer_score < 11:
                    dealer_score += 11
                else:
                    dealer_score += 1
            if dealer_aces == 2:
                if dealer_score < 10:
                    dealer_score += 12
                else:
                    dealer_score += 2
            if dealer_aces == 3:
                if dealer_score < 9:
                    dealer_score += 13
                else:
                    dealer_score += 3
            if dealer_aces == 4:
                if dealer_score < 8:
                    dealer_score += 14
                else:
                    dealer_score += 4
            if len(dealer_hand) == 1:
                print(f"Dealer Hand: {dealer_hand}", end="")  
                print(f"   Dealer has {dealer_score}")
            elif dealer_score == 21:
                print(f"Dealer Hand: {dealer_hand}", end="")
                print(f"   Dealer has {dealer_score}")
                print("Dealer wins.")
                keep_playing()
                break
            else:
                continue
        
        # Logic for player to Hit or Stand.
        while player_score < 21:
            if player_score >= 10 and player_score <= 11 and wager < bank:
                play_double = (input("Choose your play. (H)it, (S)tand, or (D)ouble. You choose to :"))
                if play_double.upper() == "D":
                    print(f"Player has doubled down. Wager increaded to ${wager * 2}")
                    bank -= wager
                    wager += wager
                    player_hand.append(deck[randint(0, len(deck) - 1)])
                    deck.remove(player_hand[-1])
                    player_score = 0
                    player_aces = 0 
                    for card in player_hand:
                        if isinstance(card.value, int):
                            player_score += card.value
                        else:
                            if card.value == "A":
                                player_aces += 1
                            else:
                                player_score += 10
                    if player_aces == 1:
                        if player_score < 11:
                            player_score += 11
                        else:
                            player_score += 1
                    if player_aces == 2:
                        if player_score < 10:
                            player_score += 12
                        else:
                            player_score += 2
                    if player_aces == 3:
                        if player_score < 9:
                            player_score += 13
                        else:
                            player_score += 3
                    if player_aces == 4:
                        if player_score < 8:
                            player_score += 14
                        else:
                            player_score += 4
                    print(f"Player Hand: {player_hand}")
                    print(f"Player has {player_score}")
                    break
                elif play_double.upper() == "H":
                    player_hand.append(deck[randint(0, len(deck) - 1)])
                    deck.remove(player_hand[-1])
                    player_score = 0
                    player_aces = 0 
                    for card in player_hand:
                        if isinstance(card.value, int):
                            player_score += card.value
                        else:
                            if card.value == "A":
                                player_aces += 1
                            else:
                                player_score += 10
                    if player_aces == 1:
                        if player_score < 11:
                            player_score += 11
                        else:
                            player_score += 1
                    if player_aces == 2:
                        if player_score < 10:
                            player_score += 12
                        else:
                            player_score += 2
                    if player_aces == 3:
                        if player_score < 9:
                            player_score += 13
                        else:
                            player_score += 3
                    if player_aces == 4:
                        if player_score < 8:
                            player_score += 14
                        else:
                            player_score += 4
                    
                    #Player Busts
                    if player_score > 21:
                        print(f"Player Hand: {player_hand}")
                        print(f"Player has {player_score}")
                        print("Player Busts.")
                        print(f"Player Bank: ${bank}")
                        keep_playing()
                        break
                    print(f"Player Hand: {player_hand}", end="")
                    print(f"   Player has {player_score}")
                elif play_double.upper() == "S":
                    print(f"Player stands at {player_score}")
                    break
            else:
                play = input("Choose your play. (H)it or (S)tand. You choose to :")
                if play.upper() == "H":
                    player_hand.append(deck[randint(0, len(deck) - 1)])
                    deck.remove(player_hand[-1])
                    player_score = 0
                    player_aces = 0 
                    for card in player_hand:
                        if isinstance(card.value, int):
                            player_score += card.value
                        else:
                            if card.value == "A":
                                player_aces += 1
                            else:
                                player_score += 10
                    if player_aces == 1:
                        if player_score < 11:
                            player_score += 11
                        else:
                            player_score += 1
                    if player_aces == 2:
                        if player_score < 10:
                            player_score += 12
                        else:
                            player_score += 2
                    if player_aces == 3:
                        if player_score < 9:
                            player_score += 13
                        else:
                            player_score += 3
                    if player_aces == 4:
                        if player_score < 8:
                            player_score += 14
                        else:
                            player_score += 4
                    
                    #Player Busts
                    if player_score > 21:
                        print(f"Player Hand: {player_hand}")
                        print(f"Player has {player_score}")
                        print("Player Busts.")
                        print(f"Player Bank: ${bank}")
                        keep_playing()
                        break
                    print(f"Player Hand: {player_hand}", end="")
                    print(f"   Player has {player_score}")
                elif play.upper() == "S":
                    print(f"Player stands at {player_score}")
                    break

        #Dealer hand logic. Dealer stands on hard 17 and over. Dealer hits on soft 17 and under.
        print(f"Dealer Hand: {dealer_hand}", end="")
        print(f"   Dealer has {dealer_score}")
        while dealer_score <= 16:
            dealer_hand.append(deck[randint(0, len(deck) - 1)])
            deck.remove(dealer_hand[-1])
            dealer_score = 0
            dealer_aces = 0
            for card in dealer_hand:
                if isinstance(card.value, int):
                    dealer_score += card.value
                else:
                    if card.value == "A":
                        dealer_aces += 1
                    else:
                        dealer_score += 10
            if dealer_aces == 1:
                if dealer_score < 11:
                    dealer_score += 11
                else:
                    dealer_score += 1
            if dealer_aces == 2:
                if dealer_score < 10:
                    dealer_score += 12
                else:
                    dealer_score += 2
            if dealer_aces == 3:
                if dealer_score < 9:
                    dealer_score += 13
                else:
                    dealer_score += 3
            if dealer_aces == 4:
                if dealer_score < 8:
                    dealer_score += 14
                else:
                    dealer_score += 4
            print(f"Dealer Hand: {dealer_hand}")
            print(f"Dealer has {dealer_score}")

            #Dealer bust
            if dealer_score > 21:
                bank += wager * 2
                print("Dealer Busts!. Player wins.")
                print(f"Player Bank : ${bank}")
                keep_playing()
                break

        # Dealer with Ace in hand
        while dealer_score == 17:
            dealer_score = 0
            dealer_aces = 0
            for card in dealer_hand:
                if isinstance(card.value, int):
                    dealer_score += card.value
                else:
                    if card.value == "A":
                        dealer_aces += 1
                    else:
                        dealer_score += 10
            if dealer_aces == 1:
                if dealer_score < 11:
                    dealer_scoree += 11
                else:
                    dealer_score += 1
            if dealer_aces == 2:
                if dealer_score < 10:
                    dealer_score += 12
                else:
                    dealer_score += 2
            if dealer_aces == 3:
                if dealer_score < 9:
                    dealer_score += 13
                else:
                    dealer_score += 3
            if dealer_aces == 4:
                if dealer_score < 8:
                    dealer_score += 14
                else:
                    dealer_score += 4
            if dealer_aces > 0:
                dealer_hand.append(deck[randint(0, len(deck) - 1)])
                deck.remove(dealer_hand[-1])
                dealer_score = 0
                dealer_aces = 0
                for card in dealer_hand:
                    if isinstance(card.value, int):
                        dealer_score += card.value
                    else:
                        if card.value == "A":
                            dealer_aces += 1
                        else:
                            dealer_score += 10
                if dealer_aces == 1:
                    if dealer_score < 11:
                        dealer_scoree += 11
                    else:
                        dealer_score += 1
                if dealer_aces == 2:
                    if dealer_score < 10:
                        dealer_score += 12
                    else:
                        dealer_score += 2
                if dealer_aces == 3:
                    if dealer_score < 9:
                        dealer_score += 13
                    else:
                        dealer_score += 3
                if dealer_aces == 4:
                    if dealer_score < 8:
                        dealer_score += 14
                    else:
                        dealer_score += 4
            else:
                break

            print(f"Dealer Hand: {dealer_hand}", end="")
            print(f"   Dealer has {dealer_score}")
        
        # Compare results and pay out winnings.

        if player_score > 21:
            print(f"Player Hand: {player_hand}")
            print(f"Player has {player_score}")
            print("Player Busts.")
            print(f"Player Bank: ${bank}")
            keep_playing()
        
        elif player_score > dealer_score and player_score <= 21:
            bank += wager * 2
            print("Player Wins!")
            print(f"Player Bank: ${bank}")
            keep_playing()

        elif dealer_score > player_score and dealer_score <= 21:
            print("Dealer wins.")
            print(f"Player Bank: ${bank}")
            keep_playing()

        else: 
            bank += wager
            print("Its a Tie.")
            print(f"Player Bank: ${bank}")
            keep_playing()
    
deal()
