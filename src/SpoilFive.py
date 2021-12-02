
import random
from PlayingCard import PlayingCard
from ConsoleInput import ConsoleInput

class SpoilFive():


    user_input=ConsoleInput()

    PlayingCard = PlayingCard()

    def set_user_input(self, user_input):
        self.user_input = user_input

    def determineTrump(self, deck):
        topCard = deck.pop()
        topCardSuit = topCard[0]
        return topCardSuit

    def start_round(self):
        NoPlayers = self.user_input.get_input("How many players are there? ")
        deck = self.PlayingCard.generate_deck()
        deck = self.PlayingCard.shuffle_cards(deck)
        listOfHands = self.PlayingCard.deal_cards(deck, 5, int(NoPlayers))
        global trump
        trump = self.determineTrump(deck)

        global cardHierarchy
        cardHierarchy = self.determineHierarchy()
        

        return listOfHands

    def player_turn(self, hand):
        for i in range(len(hand)):
            print(hand[i], end = " ")
        print(end="\n")

        cardInHand = False
        while not cardInHand:
            cardToPlay = self.user_input.get_input("Type the card you wish to play ")
            if cardToPlay in hand:
                self.PlayingCard.play_a_card(hand, cardToPlay)
                return cardToPlay
            else:
                print("That card is not in your hand")

    def bot_turn(self, hand):


player = SpoilFive()
    