from PlayingCard import PlayingCard
class Player():

    playingCard = PlayingCard()

    def __init__(self, hand):
        self.hand = hand
        self.lastPlayedCard = ""
        self.noOfTricks = 0 
    
    def playCard(self, cardToPlay):
        self.playingCard.play_a_card(self.hand, cardToPlay)

    


