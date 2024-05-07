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

    def draw(self):
        return self.deck.pop()
class Dealer:

    @staticmethod
    def startGmae (amountOfPlayers, gamemode):
        table = {
            "players": [],
            "gamemod":gamemode,
            "deck": Deck(),
        }

        table["deck"].shuffleDeck()

        for person in range(0, amountOfPlayers):
            # プレーヤの手札
            playerCard = []
            for i in range (0, Dealer.initialCards(gamemode)):
                playerCard.append(table["deck"].draw())
            table["players"].append(playerCard)

        return table
    @staticmethod
    def initialCards(gamemode):
       if gamemode == "21":
          return 2
       if gamemode == "poker":
          return 5
    @staticmethod
    def printTableInformation(table):
       print("Amount of players: " + str(len(table["players"])) + "... Game mode: " + table["gamemod"] + ". At this table: ")

       for i, player in enumerate(table["players"]):
         print(str(i + 1) + "player cards")
         for card in player:
            print(card.getCardString())
    @staticmethod
    def score21Individual(cards):
          vaule = 0
          for card in cards:
              vaule += card.intValue
          return vaule if 21 >= vaule >= 1 else 0

class HelperFunctions:

    @staticmethod
    def maxInArrayIndex(intArr):
       maxNum = 0
       maxIndex = intArr[0]
       for i,n in  enumerate(intArr):
          if n > maxIndex:
             maxIndex = i
             maxNum += i
       return maxIndex

# 最大値は19(= index 2)
arr1 = [1, 9, 19, 3, 4, 6]
print(HelperFunctions.maxInArrayIndex(arr1))

# 最大値は5(= index 0)
arr2 = [5, 2, 1, 3, 5, 5]
print(HelperFunctions.maxInArrayIndex(arr2))
