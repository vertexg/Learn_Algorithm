わからなかったためもう一度復習

def winnerBlackjack(playerCards,houseCards):
    playerScore = 0
    houseScore = 0

 
    for card in playerCards: playerScore += cardValue(card)
    for card in houseCards: houseScore += cardValue(card)

    if playerScore > 21 or playerScore == houseScore: return False

    if houseScore < 22 and houseScore > playerScore: return False
    return True

def cardValue(cardString):
    string = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    return string.index(cardString[1:]) + 1


print(winnerBlackjack(["♣4","♥7","♥7"],["♠Q","♣J"]))
