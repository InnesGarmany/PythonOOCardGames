import random
from PlayingCard import PlayingCard
from ConsoleInput import ConsoleInput
from ConsoleOutput import ConsoleOutput
from output import Output
from Player import Player

class SpoilFive():

    output = ConsoleOutput()
    

    user_input=ConsoleInput()
    PlayingCard = PlayingCard()
    leadingSuit = "S"
    trump = "H"
    hierarchy = []
    cardsPlayed = []

    def set_user_input(self, user_input):
        self.user_input = user_input

    def determineTrump(self, deck):
        topCard = deck.pop()
        topCardSuit = topCard[0]
        return topCardSuit

    def addTrump(self,trump, isRed = False, isHearts = False):
        if isRed == True:
            for i in range(8):
                self.hierarchy.append(trump + str(10-i))
            if not isHearts:
                self.hierarchy.append(trump + "A")
        else:
            for i in range(8):
                self.hierarchy.append(trump + str(i+2))
            self.hierarchy.insert(0, trump + "A")

        
        self.hierarchy.remove(trump+"5")
        self.hierarchy.insert(0,trump+"Q")
        self.hierarchy.insert(0,trump+"K")
        self.hierarchy.insert(0,"HA")
        self.hierarchy.insert(0,trump+"J")
        self.hierarchy.insert(0,trump+"5")

    def addNonTrump(self, leadingSuit, trump):
        remainingCards = self.PlayingCard.generate_deck()
        remainingCards.remove("HA")
        for card in remainingCards:
            if trump in card:
                remainingCards.remove(card)

        if leadingSuit == "D" or leadingSuit == "H":
            for i in range(8):
                self.hierarchy.append(leadingSuit + str(10-i))
                remainingCards.remove(leadingSuit + str(10-i))
            if leadingSuit == "D":
                self.hierarchy.append("DA")
                remainingCards.remove("DA")
        else:
            self.hierarchy.append(leadingSuit + "A")
            remainingCards.remove(leadingSuit + "A")
            for i in range(8):
                self.hierarchy.append(leadingSuit + str(i+2))
                remainingCards.remove(leadingSuit + str(i+2))
            
        self.hierarchy.append(leadingSuit + "J")
        remainingCards.remove(leadingSuit + "J")
        self.hierarchy.append(leadingSuit + "Q")
        remainingCards.remove(leadingSuit + "Q")        
        self.hierarchy.append(leadingSuit + "K")
        remainingCards.remove(leadingSuit+"K")


        for card in remainingCards:
            self.hierarchy.append(card)


    def setHierarchy(self, trump, leadingSuit ):
        if trump == "H":
            self.addTrump(trump, True, True)
        elif trump == "D":
            self.addTrump(trump, True)
        else:
            self.addTrump(trump)

        self.addNonTrump(leadingSuit, trump)

        return self.hierarchy

    def setLeadSuit(self, leadSuit):
        self.leadingSuit = leadSuit
        self.cardHierarchy = self.setHierarchy(self.trump, self.leadingSuit)




    def start_round(self):
        NoPlayers = self.user_input.get_input("How many players are there? ")
        deck = self.PlayingCard.generate_deck()
        deck = self.PlayingCard.shuffle_cards(deck)
        listOfHands = self.PlayingCard.deal_cards(deck, 5, int(NoPlayers))
        trump = self.determineTrump(deck)

        

        return listOfHands
    
    def start_trick(self):
        pass

    def player_turn(self, hand):
        for i in range(len(player.hand)):
            self.output.output(player.hand[i], " ")
        self.output.output("")


        cardInHand = False
        while not cardInHand:
            cardToPlay = self.user_input.get_input("Type the card you wish to play ")
            if cardToPlay in hand:
                player.playCard(hand, cardToPlay)
                self.cardsPlayed.append(cardToPlay)
                if player.isLeading == True:
                    self.setLeadSuit(cardToPlay[0])
                return cardToPlay
            else:
                self.output.output("That card is not in your hand")



    def CPU_turn(self,CPU):
        if CPU.isLeading: #The decision of which card to play first is low-impact and thus randomized
            cardToPlay = random.randint(0, len(CPU.hand))
            CPU.playCard(cardToPlay)
            self.cardsPlayed.append(cardToPlay)

        else:
            bestCard = len(self.hierarchy)+2
            worstCard = -2
            goodPlayFound = False

            for card in CPU.hand:
                for playedCard in self.cardsPlayed:
                    if self.hierarchy.find(card) < self.hierarchy.find(playedCard) and self.hierarchy.find(card) < bestCard:
                        bestCard = self.hierarchy.find(card)
                        goodPlayFound = True

                    elif self.hierarchy.find(card) > self.hierarchy.find(playedCard) and self.hierarchy.find(card) > worstCard:
                        worstCard = self.hierarchy.find(card)
                        
            if goodPlayFound:
                CPU.playCard(bestCard)
                self.cardsPlayed.append(bestCard)
                self.output.output(bestCard + " has been played. The cards in play are " + self.cardsPlayed)
            else: 
                CPU.playCard(worstCard)
                self.cardsPlayed.append(worstCard)
                self.output.output(bestCard + " has been played. The cards in play are " + self.cardsPlayed)



    
CPUdict = {}
spoilFive = SpoilFive(True)
listOfHands = spoilFive.start_round()
player = Player(listOfHands.pop())
i=0
for hand in listOfHands:
    i+=1
    CPUdict["CPU"+str(i)] = Player(hand)


