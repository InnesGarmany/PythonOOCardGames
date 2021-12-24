from PlayingCard import PlayingCard
class Player():

    playingCard = PlayingCard()

    def __init__(self, hand, isLeading = "False"):
        self.hand = hand
        self.isLeading = isLeading
        self.lastPlayedCard = ""
    
    def playCard(self, cardToPlay):
        self.playingCard.play_a_card(self.hand, cardToPlay)

    


