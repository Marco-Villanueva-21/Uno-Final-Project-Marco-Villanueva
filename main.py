import random

deck = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'RS', 'RR', 'R+2', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'BS', 'BR', 'B+2', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'YS', 'YR', 'Y+2', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'GS', 'GR', 'G+2', 'W', 'W+4']

playerDeck = []
cpu1Deck = []
cpu2Deck = []
cpu3Deck = []

for x in range (0,7):
  cDeck = random.choice(deck)
  playerDeck.append(cDeck)
for x in range (0,7):
  cDeck = random.choice(deck)
  cpu1Deck.append(cDeck)
for x in range (0,7):
  cDeck = random.choice(deck)
  cpu2Deck.append(cDeck)
for x in range (0,7):
  cDeck = random.choice(deck)
  cpu3Deck.append(cDeck)

pDeck = ', '.join(str(x) for x in playerDeck)

print('Welcome to UNO!')
print('The rules are simple, you have to match the color or number of the card in your hand with the card and be the first player to get rid of all of your cards. Be sure to call UNO if you only have one card left!') 
print('Cards with an "S" at the end will skip the next player')
print('Cards with an 'R' at the end will reverse the order of the players')
print('Cards with a "W" will allow you to pick a color')
print('Cards with a "+2" or "+4" will give the next player 2 or 4 cards if they cannot add on to the +2 or +4')

#give user a random 7-card deck
print('Here is your deck!')
print(str(pDeck))

#give 3 computer players a 7-card deck

c1Deck = ', '.join(str(x) for x in cpu1Deck)

c2Deck = ', '.join(str(x) for x in cpu2Deck)

c3Deck = ', '.join(str(x) for x in cpu3Deck)

#tell user what card is on top of the playing pile

face = random.choice(deck)
print("The current card on the playing pile is:", str(face))

#check if the user's deck has a valid card to play
def checkValid(card):
  long = len(face)
  if card[0:long] == face[0:long]:
#if not, draw a card from the deck
#ask user if they want to draw or play a card
#ask user what card they want to play
#if user plays a card that is a valid play, remove it from their deck and add it to the playing pile
#make next computer player play a valid card from their deck and tell the user their placed card
#if a player reaches zero cards, display the winner