import random

deck = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'RS', 'RR', 'R2+', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'BS', 'BR', 'B2+', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'YS', 'YR', 'Y2+', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'GS', 'GR', 'G2+', 'WC', 'W4+']

playerDeck = []
cpu1Deck = []
cpu2Deck = []
cpu3Deck = []
valid = False
played = False

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
print('Cards with a "2+" or "4+" will give the next player 2 or 4 cards if they cannot add on to the 2+ or 4+')

#give user a random 7-card deck
print('Here is your deck!')
print(str(pDeck))

#give 3 computer players a 7-card deck

c1Deck = ', '.join(str(x) for x in cpu1Deck)

c2Deck = ', '.join(str(x) for x in cpu2Deck)

c3Deck = ', '.join(str(x) for x in cpu3Deck)

#tell user what card is on top of the playing pile

face = str(random.choice(deck))
print("The current card on the playing pile is:", face)

#function to check if the user's deck has a valid card to play
def checkValid(playCard):
  if playCard[0] == face[0] or playCard[1] == face[1]:
    return True
  else:
    return False

#function for drawing a card
def drawnCard(add):

  #check if the drawn card is valid
  if checkValid(add):
    PD = input('You drew a valid card! Play or skip?: ').lower()

    #player asks to play
    if PD == 'play':
      face = add
      playerDeck.remove(add)
      print('You played', add)
      print('The current card on the playing pile is:', face)

    #player asks to skip
    elif PD == 'skip':
      print('You skipped your turn!')

  #if the card is invalid, skip the player's turn
  else:
    print('You drew an invalid card! You must skip your turn!')

#check each card in the user's deck
for x in range (0, len(playerDeck)):
  print (playerDeck[0+x])
  if checkValid(playerDeck[0+x]):
    valid = True
    
#if the user has a valid card, ask if they wish to play or draw
if valid == True:
  PD = input('Play or Draw?: ').lower()

  #enter a loop that loops back if the user inputs an invalid response
  while played == False:

    #if the user inputs play, ask them which card they wish to play
    if PD == 'play':
      playCard = input('What card would you like to play?: ').upper()

      #check if the card is in the user's deck and is a valid card
      if playCard in playerDeck and checkValid(playCard):
        face = playCard
        playerDeck.remove(playCard)
        print('You played', playCard)
        print('The current card on the playing pile is:', face)
        pDeck = ', '.join(str(x) for x in playerDeck)
        print('Your deck is:', str(pDeck))
        played = True

      #if the card is not in the user's deck, ask them to input a valid card
      else:
        print('That is an invalid card')
        pDeck = ', '.join(str(x) for x in playerDeck)
        print('Your deck is:', str(pDeck))
        played = False

    #if the user inputs draw, draw a card
    elif PD == 'draw':
      add = random.choice(deck)
      playerDeck.append(add)
      print('You drew a', add)
      played = True
      drawnCard(add)

#if user does not have a valid card, force to draw and ask if they want to play or skip
if valid == False:
  print('You do not have a valid card to play')
  add = random.choice(deck)
  playerDeck.append(add)
  print('You drew a', add)
  drawnCard(add)
       
#skip cards will skip the next player
#reverse cards will reverse the order of the players
#wild cards will allow the user to pick a color
#2+ or 4+ cards will force the next player 2 or 4 cards
#if not, draw a card from the deck
#ask user if they want to draw or play a card
#ask user what card they want to play
#if user plays a card that is a valid play, remove it from their deck and add it to the playing pile
#make next computer player play a valid card from their deck and tell the user their placed card
#if a player reaches zero cards, display the winner