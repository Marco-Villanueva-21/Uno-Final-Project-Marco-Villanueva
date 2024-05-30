import random

deck = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'RS', 'RR', 'R2+', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'BS', 'BR', 'B2+', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'YS', 'YR', 'Y2+', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'GS', 'GR', 'G2+', 'WC', 'W4+']

special = ['S', 'R']
colors = ['R', 'B', 'Y', 'G']

print('Welcome to UNO!')
print('\nThe rules are simple, you have to match the color or number of the card in your hand with the card and be the first player to get rid of all of your cards. Be sure to call UNO if you only have one card left!') 
print('Cards with an "S" at the end will skip the next player')
print('Cards with an 'R' at the end will reverse the order of the players')
print('Cards with a "W" will allow you to pick a color')
print('Cards with a "2+" or "4+" will give the next player 2 or 4 cards if they cannot add on to the 2+ or 4+')

gameExit = True
gameLoop = True

#tell user what card is on top of the playing pile

face = str(random.choice(deck))
print("The current card on the playing pile is:", face)

#decide whose turn it currently is
def currentTurn():
  global turnNum
  if turnNum > 4:
    turnNum = 0
  if turnNum < 0:
    turnNum = 4
  playTurn = turn[turnNum]
  return playTurn
  
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

#define the play again checker at the end of the game
def playMore():
  global playAgainCheck
  global playAgain
  while not playAgainCheck:
    if playAgain == 'Y':
      playAgainCheck = True
      gameExit = True
    elif playAgain == 'N':
      playAgainCheck = True
      gameExit = False
    else:
      playAgain = False
      
#define skip cards (the next player's turn is skipped)
def skip():
  global turnNum
  global playTurn
  if playCard[1] == 'S':
    turnNum = turnNum + (reverse*1)
    playTurn = currentTurn()
    print(playTurn, 'had their turn skipped!')

#define reverse cards (the order of the players reverse)
def rev():
  global reverse
  if playCard[1] == 'R':
    reverse = reverse*(-1)
    print('The order of the players has been reversed!')

#define plus cards (2 or 4 cards are forced to be added to the next player's deck and the next player's turn is skipped)
def plus():
  global turnNum
  global reverse
  if playCard[1] == '2' or playCard[1] == '4':
    turnNum = turnNum + (reverse*1)

    #user is hit
    if currentTurn() == 'user':
      for x in range(0, int(playCard[1])):
        cDeck = random.choice(deck)
        playerDeck.append(cDeck)
        print('You drew', cDeck)
      print('Your turn was skipped!')
      
    #CPU1 is hit
    if currentTurn() == 'cpu1':
      for x in range(0,int(playCard[1])):
        cDeck = random.choice(deck)
        cpu1Deck.append(cDeck)
      print('CPU1 drew two cards!')

    #CPU2 is hit
    if currentTurn() == 'cpu2':
      for x in range(0,int(playCard[1])):
        cDeck = random.choice(deck)
        cpu2Deck.append(cDeck)
      print('CPU2 drew two cards!')

    #CPU3 is hit
    if currentTurn() == 'cpu3':
      for x in range(0,int(playCard[1])):
        cDeck = random.choice(deck)
        cpu3Deck.append(cDeck)
      print('CPU3 drew two cards!')
    turnNum = turnNum + (reverse*1)
    print(turn, 'had their turn skipped!')
      

#enter a game loop that loops back after the game ends and the user wishes to play again
while gameExit == True:
  #define variables
  playerDeck = []
  cpu1Deck = []
  cpu2Deck = []
  cpu3Deck = []
  turn = ['user', 'cpu1', 'cpu2', 'cpu3']
  turnNum = 0
  reverse = 1
  valid = False
  played = False
  playAgain = 'Y'
  playAgainCheck = False

   #give the user and 3 computer players a 7-card deck
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

  #turn the user's deck list into strings 
  pDeck = ', '.join(str(x) for x in playerDeck)

  #give user a random 7-card deck
  print('\nHere is your deck!')
  print(str(pDeck))

  while gameLoop:
    if currentTurn() == 'user':
      #check each card in the user's deck
      for x in range (0, len(playerDeck)):
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
    
            #if the card is not in the user's deck, ask them to input a valid card
            if playCard not in playerDeck and playCard[0] != 'W':
              print('That is an invalid card')
              pDeck = ', '.join(str(x) for x in playerDeck)
              print('Your deck is:', str(pDeck))
              played = False
      
            #check if the card is in the user's deck
            if playCard in playerDeck:
    
              #check if the played card is a wild card
              chooseColor = False
              if playCard[0] == 'W':
                #wild cards will allow the user to pick a color
                print('You played a Wild Card!')
                while chooseColor == False:
                  color = input('What color would you like to change it to?: ').upper()
    
                  #if the user inputs a valid color, change the card to that color
                  if color in colors:
                    face = color + 'C'
                    print('You changed the color to', color)
                    print('The current card on the playing pile is:', face)
                    chooseColor = True
                    played = True
                  else: 
                    print('You picked an invalid color! Please try again!')
                    chooseColor = False
    
              #otherwise, check if the card is playable
              elif checkValid(playCard):
                face = playCard
                playerDeck.remove(playCard)
                print('You played', playCard)
      
                if playCard[1] in special or len(playCard) == 2:
                  print('you played a special card!')
                  skip()
                  rev()
                  plus()
                
                print('The current card on the playing pile is:', face)
                pDeck = ', '.join(str(x) for x in playerDeck)
                print('Your deck is:', str(pDeck))
                played = True
      
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
      turnNum = turnNum + (1*reverse)
    
    if currentTurn() == 'cpu1':
      print("It is CPU1's turn!")
      print("CPU1 has", len(cpu1Deck), "cards")

    if currentTurn() == 'cpu2':
      print("It is CPU2's turn!")
      print("CPU2 has", len(cpu2Deck), "cards")

    if currentTurn() == 'cpu3':
      print("It is CPU3's turn!")
      print("CPU3 has", len(cpu3Deck), "cards")
  #make next computer player play a valid card from their deck and tell the user their placed card
  #if a player reaches zero cards, display the winner
    if len(playerDeck) == 0:
      print('You win!')
      gameLoop = False
      playAgain = input('Would you like to play again? (Y/N): ').upper()
      playMore()
    if len(cpu1Deck) == 0:
      print('CPU1 wins!')
      gameLoop = False
      playAgain = input('Would you like to play again? (Y/N): ').upper()
      playMore()
    if len(cpu2Deck) == 0:
      print('CPU2 wins!')
      gameLoop = False
      playAgain = input('Would you like to play again? (Y/N): ').upper()
      playMore()
    if len(cpu3Deck) == 0:
      print('CPU3 wins!')
      gameLoop = False
      playAgain = input('Would you like to play again? (Y/N): ').upper()
      playMore()