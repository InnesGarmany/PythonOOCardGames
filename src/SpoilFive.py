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
    
    lastWinner = 0

    def __init__(self, cardsPlayed=[]):
        self.cardsPlayed = cardsPlayed

    def set_user_input(self, user_input):
        self.user_input = user_input

    def determineTrump(self, deck):
        topCard = deck.pop()
        topCardSuit = topCard[0]
        return topCardSuit

    def addTrump(self,trump, isRed = False, isHearts = False):
        if isRed == True:
            for i in range(9):
                self.hierarchy.append(trump + str(10-i))
            if not isHearts:
                self.hierarchy.append(trump + "A")
        else:
            for i in range(9):
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
        if leadingSuit != trump:
            for card in remainingCards:
                if trump in card:
                    remainingCards.remove(card)

        if leadingSuit == "D" or leadingSuit == "H":
            for i in range(9):
                self.hierarchy.append(leadingSuit + str(10-i))
                remainingCards.remove(leadingSuit + str(10-i))
            if leadingSuit == "D":
                self.hierarchy.append("DA")
                remainingCards.remove("DA")
        else:
            self.hierarchy.append(leadingSuit + "A")
            remainingCards.remove(leadingSuit + "A")
            for i in range(9):
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
        if self.lastWinner == 0:
            player.playCard(self.player_turn(players[0]))
        else:
            players[self.lastWinner].playCard(self.CPU_turn(players[self.lastWinner], True))

    def player_turn(self, playerOBJ, isLeading=False):
        self.output.output("This is your hand")
        for i in range(len(playerOBJ.hand)):
            self.output.output(playerOBJ.hand[i], " ")
        self.output.output("")
        
        cardInHand = False
        while not cardInHand:
            cardToPlay = self.user_input.get_input("Type the card you wish to play ")
            if cardToPlay in playerOBJ.hand:
                if isLeading:
                    self.cardsPlayed.append(cardToPlay)  
                    self.setLeadSuit(cardToPlay[0])
                    return cardToPlay
                else:
                    cardIllegal = True
                    while cardIllegal:
                        cardIllegal = False
                        if cardToPlay[0] != self.trump and cardToPlay[0] != self.leadingSuit:
                            for card in playerOBJ.hand:
                                if card[0] == self.trump or card[0] == self.leadingSuit:
                                    cardIllegal = True
                                    self.output.output("That card is illegal!")
                                    cardToPlay = self.user_input.get_input("Type the card you wish to play")

                    
                        
                    self.cardsPlayed.append(cardToPlay)
                    return cardToPlay
            else:
                self.output.output("That card is not in your hand")

    def CPU_turn(self,CPU, isLeading=False):
        if isLeading: #The decision of which card to play first is low-impact and thus randomized
            cardToPlay = random.randint(0, len(CPU.hand)-1)
            self.setLeadSuit(CPU.hand[cardToPlay][0])
            self.cardsPlayed.append(CPU.hand[cardToPlay])
            return CPU.hand[cardToPlay]

        else:
            bestCard = len(self.hierarchy)+2
            worstCard = -2
            goodPlayFound = False

            for card in CPU.hand:
                for playedCard in self.cardsPlayed:
                    if self.hierarchy.index(card) < self.hierarchy.index(playedCard) and self.hierarchy.index(card) < bestCard:
                        bestCard = self.hierarchy.index(card)
                        goodPlayFound = True

                    elif self.hierarchy.index(card) > self.hierarchy.index(playedCard) and self.hierarchy.index(card) > worstCard:
                        worstCard = self.hierarchy.index(card)
                        
            if goodPlayFound:
                self.cardsPlayed.append(self.hierarchy[bestCard])
                self.output.output(self.hierarchy[bestCard] + " has been played. The cards in play are " + str(self.cardsPlayed))
                return self.hierarchy[bestCard]
            else: 
                self.cardsPlayed.append(self.hierarchy[worstCard])
                self.output.output(self.hierarchy[worstCard] + " has been played. The cards in play are " + str(self.cardsPlayed))
                return self.hierarchy[worstCard]

    
CPUdict = {}
spoilFive = SpoilFive()
listOfHands = spoilFive.start_round()
player = Player(listOfHands.pop())
i=0
players = [player]
for hand in listOfHands:
    i+=1
    CPUdict["CPU"+str(i)] = Player(hand)

    players.append(CPUdict["CPU"+str(i)])

