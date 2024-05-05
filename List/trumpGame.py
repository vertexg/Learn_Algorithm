import random
class Card:
    def __init__(self, value, suit, intValue) :
      self.suit = suit
      self.intValue = intValue
      self.value = value
    def getCardString(self):
      return self.suit  + self.value +"(" + str(int(self.intValue)) + ")"

class Deck:
    def __init__(self):
      self.deck = self.generateDeck()

    @staticmethod
    def generateDeck():
      newDeck = []
      values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
      suits = ["♣", "♦", "♥", "♠"]

      for suit in suits:
        for i , value in enumerate(values):
           newDeck.append(Card(value, suit, i + 1))
      return newDeck

    def printDeck(self):
     print("Displaying cards...")
     for i in self.deck:
        print(i.getCardString())

    def shuffleDeck(self):
       size = len(self.deck)
       for i in range(size - 1, 0, -1):
            j = random.randint(i, size -1)
            temp = self.deck[i]
            self.deck[i] = self.deck[j]
            self.deck[j] = temp

card  = Deck()
card.printDeck()

card.shuffleDeck()
card.printDeck()

