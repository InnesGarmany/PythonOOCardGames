
import random
from PlayingCard import PlayingCard
from ConsoleInput import ConsoleInput

class SpoilFive():


    user_input=ConsoleInput()

    PlayingCard = PlayingCard()

    def set_user_input(self, user_input):
        self.user_input = user_input


    def start_round(self):
        NoPlayers = int(self.user_input.get_input("How many players are there? "))
        deck = self.PlayingCard.generate_deck()
        deck = self.PlayingCard.shuffle_cards(deck)
        listOfHands = self.PlayingCard.deal_cards(deck, 5, NoPlayers)
        return listOfHands
    
game=SpoilFive()
print(game.start_round())