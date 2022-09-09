# Bonus Question - 1
from random import randint

def createDeck():
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
    suits = ["s", "h", "d", "c"]
    cards = []
    for i in suits:
        for j in values:
            cards.append(j+i)
    return cards

def shuffledDeck(cards :list):
    for i in range(0,52):
        randomIndex = randint(0, 51)
        swapVal = cards[i]
        cards[i] = cards[randomIndex]
        cards[randomIndex] = swapVal
    return cards

if __name__ == "__main__":
    cardDeck = createDeck()
    print(f" Card Deck:\n{str(cardDeck)}")
    print(f" Shuffled Card Deck:\n{str(shuffledDeck(cardDeck))}")