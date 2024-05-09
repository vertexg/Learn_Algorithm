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

 @staticmethod
  
    def winnerOf21(table):
        points = []
        cache = {}
        for cards in table["players"]:
            point = Dealer.score21Individual(cards)
            # pointを配列に保存
            points.append(point)
            if point in cache:
                cache[point] += 1
            else:
                cache[point] = 1

        print(points)

        winnerIndex = HelperFunctions.maxInArrayIndex(points)
        if cache[points[winnerIndex]] > 1:
            return "It is a draw"
        elif cache[points[winnerIndex]] >= 0:
            return "player " + str(winnerIndex + 1) + " is the winner"
        else:
            return "No winners.."

class HelperFunctions:

    @staticmethod
    def maxInArrayIndex(intArr):
        maxIndex = 0
        maxValue = intArr[0]
        for i, num in enumerate(intArr):
            if num > maxValue:
                maxValue = num
                maxIndex = i

        return maxIndex

table = Dealer.startGame(4, "21")
Dealer.printTableInformation(table)
print(Dealer.winnerOf21(table))
