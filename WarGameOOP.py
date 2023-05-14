# WAR  CARD GAME#
# Deal out by all the cards, so each player has 26 cards
# Both of these players are now turn their top card as faceup and put them on the table.
# Whoever turned the highest card, take by both of these cards and add them (face down) to the bottom of the player's packet.
# Then both of these players need to turn up their next card and so on.
# If the two cards played are of equal value, then there is a "war".
# Both players place the next card from their pile face down and then another card face-up.
# The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck.
# If the face-up cards are again equal then the battle repeats with another set of face-down/up cards.
# This repeats until one player's face-up card is higher than their opponent's
#####################################################################################################################################


import randomg


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank+" of "+self.suit


class Deck:
    def __init__(self):
        self.allCards = []

        for suit in suits:
            for rank in ranks:
                createdCard = Card(suit, rank)
                self.allCards.append(createdCard)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.allCards)

    def dealOne(self):
        return self.allCards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.allCards = []

    def removeOne(self):
        return self.allCards.pop(0)

    def addCards(self, newCards):
        if type(newCards) == type([]):
            self.allCards.extend(newCards)
        else:
            self.allCards.append(newCards)

    def __str__(self):
        return f"Player {self.name} has {len(self.allCards)}"


# Game setup

playerOne = Player("One")
playerTwo = Player("Two")

deck = Deck()

for card in range(26):
    playerOne.addCards(deck.dealOne())
    playerTwo.addCards(deck.dealOne())

roundNum = 0
gameOn = True

while gameOn:
    roundNum += 1
    print(f"Round {roundNum}")

    if len(playerOne.allCards) == 0:
        print("Player One,out of cards! Playr Two Wins!!")
        gameOn = False
        break

    if len(playerTwo.allCards) == 0:
        print("Player Two,out of cards! Playr One Wins!!")
        gameOn = False
        break

    # Start a new round

    # Current cards on field
    playerOneCards = []
    playerOneCards.append(playerOne.removeOne())

    # Current cards on field
    playerTwoCards = []
    playerTwoCards.append(playerTwo.removeOne())

    atWar = True

    while atWar:
        if playerOneCards[-1].value > playerTwoCards[-1].value:
            playerOne.addCards(playerOneCards)
            playerOne.addCards(playerTwoCards)
            atWar = False

        elif playerTwoCards[-1].value > playerOneCards[-1].value:
            playerTwo.addCards(playerOneCards)
            playerTwo.addCards(playerTwoCards)
            atWar = False

        else:
            print("WAR!!")

            if len(playerOne.allCards) < 3:
                print("Player One unbale to declare war")
                print("Player Two Wins")
                gameOn = False
                break

            elif len(playerTwo.allCards) < 3:
                print("Player Two unbale to declare war")
                print("Player One Wins")
                gameOn = False
                break
            else:
                for num in range(3):
                    playerOneCards.append(playerOne.removeOne())
                    playerTwoCards.append(playerTwo.removeOne())
