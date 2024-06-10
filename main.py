import random
import time

deck = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'RS', 'RR', 'R+2', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'BS', 'BR', 'B+2', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'YS', 'YR', 'Y+2', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'GS', 'GR', 'G+2', 'WC', 'W+4']

special = ['S', 'R', '+']
colors = ['R', 'B', 'Y', 'G']

print('Welcome to UNO!')
print('\nThe rules are simple, you have to match the color or number of the card in your hand with the playing pile card and be the first player to get rid of all of your cards. Be sure to call UNO if you only have one card left!') 
print('Cards with an "S" at the end will skip the next player')
print('Cards with an 'R' at the end will reverse the order of the players')
print('Cards with a "W" will allow you to pick a color')
print('Cards with a "+2" or "+4" will give the next player 2 or 4 cards if they cannot add on to the +2 or +4')

gameExit = True

#decide whose turn it currently is
def currentTurn():
  global turnNum
  if turnNum > 3:
    turnNum = 0
  if turnNum < 0:
    turnNum = 3
  playTurn = turn[turnNum]
  return playTurn
  
#function to check if the user's deck has a valid card to play
def checkValid(playCard):
  if playCard[0] == face[0] or playCard[1] == face[1] or playCard[0] == 'W':
    return True
  else:
    return False

#function for drawing a card
def drawnCard(add):
  global face
  
  validResponse = False
  while not validResponse:
    
    #check if the drawn card is valid
    if checkValid(add):
      PD = input('You drew a valid card! Play or skip?: ').lower()
  
      #player asks to play
      if PD == 'play':
        face = add

        #check if the drawn card is a wild card
        if add[0] == 'W' and len(add) == 3:
          face = wild(add)
          plus(add)
          
        elif add[0] == 'W':
          wild(add)

          #check if the second character is in the special list or has three characters (meaning it must be a +2 or +4)
        elif add[1] in special: 
          print('You played a special card!')
          skip(add)
          rev(add)
          plus(add)

        #basic card is played
        else:
          print('You played', add)
          print('The current card on the playing pile is:', face)
        validResponse = True
  
      #player asks to skip
      elif PD == 'skip':
        print('You skipped your turn!')
        validResponse = True

      else:
        print('You inputted an invalid response, please try again')
        validResponse = False
  
    #if the card is invalid, skip the player's turn
    else:
      print('You drew an invalid card! You must skip your turn!')
      validResponse = True

#define CPU's ability to draw a card
def drawnCardCPU(add):
  global playTurn
  global turnNum
  
  playTurn = currentTurn()
  
  if checkValid(add):
    face = add
    cpuDeck.remove(add)
    print(playTurn, 'played', add)
    print('The current card on the playing pile is:', face)

  else:
    print(playTurn, 'skipped their turn!')

#define function to count how many cards of each color the CPU has
def countColor(cpuDeck):
  redCount = 0
  blueCount = 0
  greenCount = 0
  yellowCount = 0
  
  for x in range(0, len(cpuDeck)):
    if cpuDeck[x][0] == 'R':
      redCount = redCount + 1
    if cpuDeck[x][0] == 'B':
      blueCount = blueCount + 1
    if cpuDeck[x][0] == 'G':
      greenCount = greenCount + 1
    if cpuDeck[x][0] == 'Y':
      yellowCount = yellowCount + 1

  return redCount, blueCount, greenCount, yellowCount

def cpuTurn(cpuDeck):
  global turnNum
  global face
  
  playTurn = currentTurn()
  validCards = []
  valid = False
  specialPlayed = False
  
  #check each card in the cpu's deck
  for x in range (0, len(cpuDeck)):
    if checkValid(cpuDeck[0+x]):
      valid = True
      validCards.append(cpuDeck[0+x])

  #if the cpu has a valid card, check for a special card
  if valid:
    for x in range (0, len(validCards)):
      
      #if a special card is found, play it
      if validCards[0+x][1] in special or validCards[0+x][0] == 'W':

        specialPlayed = True
        cpuWild(validCards[0+x], cpuDeck)
        skip(validCards[0+x])
        rev(validCards[0+x])
        plus(validCards[0+x])
        break

    #check if a special card was not played and play a random card from the validCards list
    if not specialPlayed:
      playCard = random.choice(validCards)
      face = playCard
      cpuDeck.remove(playCard)
      print(playTurn, 'played', playCard)

      print('The current card on the playing pile is:', face)

  #if cpu does not have a valid card, force to draw and play if possible, otherwise skip their turn
  if not valid:
    add = random.choice(deck)
    cpuDeck.append(add)
    print(playTurn, 'drew a card!')
    drawnCard(add)
  turnNum = turnNum + (1*reverse)

#define the play again checker at the end of the game
def playMore():
  global playAgainCheck, playAgain, gameExit
  
  while not playAgainCheck:
    if playAgain == 'Y':
      print("Let's play again!")
      playAgainCheck = True
      gameExit = True
    elif playAgain == 'N':
      print('\nThanks for playing!')
      playAgainCheck = True
      gameExit = False
    else:
      playAgain = False

#decide how a cpu plays a wild card
def cpuWild(playCard, cpuDeck):
  global turnNum
  global face
  countedColors = []
  possible = []
  
  playTurn = currentTurn()
  if playCard[0] == 'W':
    
    print(playTurn, 'has played a wild card!')
    redCount, blueCount, greenCount, yellowCount = countColor(cpuDeck)
    
    countedColors.append(redCount)
    countedColors.append(blueCount)
    countedColors.append(greenCount)
    countedColors.append(yellowCount)

    mostColor = max(countedColors)

    if mostColor == redCount:
      possible.append('R')
    if mostColor == blueCount:
      possible.append('B')
    if mostColor == greenCount:
      possible.append('G')
    if mostColor == yellowCount:
      possible.append('Y')

    chosenColor = random.choice(possible)

    face = chosenColor + 'C'
    cpuDeck.remove(playCard)
    print(playTurn, 'changed the color to', chosenColor)
    print('The current card on the playing pile is:', face)
    return face
    
#define wild cards used by user (user can choose a color)
def wild(playCard):
  chooseColor = False

  if playCard[0] == 'W':
    
    #wild cards will allow the user to pick a color
    print('You played a Wild Card!')
    while chooseColor == False:
      color = input('What color would you like to change it to? (R, G, B, Y): ').upper()
  
      #if the user inputs a valid color, change the card to that color
      if color in colors:
        face = color + 'C'
        playerDeck.remove(playCard)
        print('You changed the color to', color)
        print('The current card on the playing pile is:', face)
        chooseColor = True
        played = True
        return face

      #otherwise, tell the user they input an invalid color and loop
      else: 
        print('You picked an invalid color! Please try again!')
        chooseColor = False
          
#define skip cards (the next player's turn is skipped)
def skip(playCard):
  global turnNum
  playTurn = currentTurn()
  
  if playCard[1] == 'S':
    print(playTurn, 'played', playCard, 'which is a skip card!')
    turnNum = turnNum + (reverse*1)
    playTurn = currentTurn()
    print(playTurn, 'had their turn skipped!')

#define reverse cards (the order of the players reverse)
def rev(playCard):
  global reverse
  playTurn = currentTurn()
  
  if playCard[1] == 'R':
    reverse = reverse*(-1)
    print(playTurn, 'played', playCard, 'which is a reverse card!')
    print('The order of the players has been reversed!')

#define plus cards (2 or 4 cards are forced to be added to the next player's deck and the next player's turn is skipped)
def plus(playCard):
  global turnNum, reverse, forceDraw

  playTurn = currentTurn()

  if playCard[1] == '+':
    if playCard[2] == '2' or playCard[2] == '4':
      defended = True
      forceDraw = int(playCard[2])
      print(playTurn, 'played', playCard, 'which is a plus card!')
  
      #loop back when a player has successfully defended a plus card
      while defended:
        plusDetected = False
    
        #check if the played card is a plus card
        if playCard[1] == '+':
          if playCard[2] == '2' or playCard[2] == '4':
            turnNum = turnNum + (reverse*1)
        
            #user is hit
            if currentTurn() == 'user':
              validResponse = False
    
              #check the user's deck for a plus card
              for x in range(0, len(playerDeck)):
                
                if '+' in playerDeck[0+x][1]:
                  plusDetected = True
    
              #if found, the game will ask the user to defend or draw
              if plusDetected:
                while not validResponse:

                  #tell the user their deck and ask if they want to defend or draw
                  pDeck = ', '.join(str(x) for x in playerDeck)
                  print('Your deck is:', str(pDeck))
                  defend = input('You have a +2 or +4 card! Defend or draw?: ').lower()
    
                  #if the user chooses to defend, the user will play their plus card to add on to the forced cards drawn and force the next player to draw
                  if defend == 'defend':
                    validResponse = True
                    plusTrue = False
                    turnNum = turnNum + (reverse*1)

                    #ask the user to play the plus card
                    while not plusTrue:
                      defence = input('Play the +2 or +4 card!: ')

                      #check if the played card is a plus card and in the user's deck
                      if defence in playerDeck and defence[1] == '+':
                        face = defence
                        playerDeck.remove(defence)
                        print('You played', defence)
                        forceDraw = forceDraw + int(defence[2])
                        plusTrue = True
                        defended = True

                      #otherwise, tell the user they inputted an invalid card and loop
                      else:
                        print('That is not a valid card! Please input a plus card from your deck!')
                        plusTrue = False  

                  #if the user chooses to draw, the user will draw the forced cards and skip their turn
                  elif defend == 'draw':
                    validResponse = True
                    for x in range(0, forceDraw):
                      cDeck = random.choice(deck)
                      playerDeck.append(cDeck)
                      print('You drew', cDeck)
                    print('You drew', forceDraw, 'cards!')
                    defended = False

                  #loop back if the user inputs an invalid response
                  else:
                    print('That is not a valid response! (type "defend" or "draw")')
                    validResponse = False

              #force the user to draw and skip their turn if a plus card is not found
              else:
                time.sleep(0.5)
                print('You don\'t have a plus card! You must draw and skip your turn!')
                for x in range(0, forceDraw):
                  cDeck = random.choice(deck)
                  playerDeck.append(cDeck)
                  defended = False
                  print('You drew', cDeck)
                  time.sleep(0.25)
                print('\nYou drew', forceDraw, 'cards in total! Yikes!')
                
            #CPU1 is hit
            if defended == True:
              if currentTurn() == 'CPU1':
                cpu1Defended = cpuDefend(cpu1Deck)

                #if CPU1 fails to defend, force to draw and skip their turn
                if cpu1Defended == False:
                  time.sleep(0.5)
                  for x in range(0,forceDraw):
                    cDeck = random.choice(deck)
                    cpu1Deck.append(cDeck)
                  defended = False
                  print('\nCPU1 drew', forceDraw, 'cards!')
                  print("CPU1 has", len(cpu1Deck), "card(s)")
          
            #CPU2 is hit
            if defended == True:
              if currentTurn() == 'CPU2':
                cpu2Defended = cpuDefend(cpu2Deck)

                #if CPU2 fails to defend, force to draw and skip their turn
                if cpu2Defended == False:
                  time.sleep(0.5)
                  for x in range(0,forceDraw):
                    cDeck = random.choice(deck)
                    cpu2Deck.append(cDeck)
                  defended = False
                  print('\nCPU2 drew', forceDraw, 'cards!')
                  print("CPU2 has", len(cpu2Deck), "card(s)")
        
            #CPU3 is hit
            if defended == True:
              if currentTurn() == 'CPU3':
                cpu3Defended = cpuDefend(cpu3Deck)

                #if CPU3 fails to defend, force to draw and skip their turn
                if cpu3Defended == False:
                  time.sleep(0.5)
                  for x in range(0,forceDraw):
                    cDeck = random.choice(deck)
                    cpu3Deck.append(cDeck)
                  defended = False
                  print('\nCPU3 drew', forceDraw, 'cards!')
                  print("CPU3 has", len(cpu3Deck), "card(s)")

      #tell the user whose turn was skipped
      playTurn = currentTurn()
      print(playTurn, 'had their turn skipped!')

#define a function for CPU players to defend a plus card
def cpuDefend(cpuDeck):
  global forceDraw, turnNum, face
  
  playTurn = currentTurn()

  #go through each card in the CPU's deck
  for x in range(0, len(cpuDeck)):
    
    #play the first plus card found if possible
    if '+' in cpuDeck[0+x][1]:
      time.sleep(0.5)
      forceDraw = forceDraw + int(cpuDeck[0+x][2])
      print('\n')
      print(playTurn, 'played', cpuDeck[0+x], 'to defend the plus card!')
      face = cpuDeck[0+x]
      cpuDeck.remove(cpuDeck[0+x])
      defended = True
      cDefended = True
      turnNum = turnNum + (reverse*1)
      return (cDefended, face)

  #otherwise, return false
  return False

#enter a game loop that loops back after the game ends and the user wishes to play again
while gameExit == True:
  
  #define variables
  playerDeck = []
  cpu1Deck = []
  cpu2Deck = []
  cpu3Deck = []
  cpuDeck = []
  turn = ['user', 'CPU1', 'CPU2', 'CPU3']
  turnNum = 0
  reverse = 1
  valid = False
  played = False
  playAgain = 'Y'
  playAgainCheck = False
  gameLoop = True

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

  #tell user what card is on top of the playing pile

  face = 'B+2'#str(random.choice(deck))
  print("The current card on the playing pile is:", face)

  while gameLoop:
    played = False
    
    if currentTurn() == 'user':

      #tell the user it is their turn, their deck and the playing pile
      pDeck = ', '.join(str(x) for x in playerDeck)
      print('\nIt is your turn!')
      print('Your deck is:', pDeck)
      print('The current card on the playing pile is:', face)
      
      #check each card in the user's deck
      for x in range (0, len(playerDeck)):
        if checkValid(playerDeck[0+x]):
          valid = True
          
      #if the user has a valid card, ask if they wish to play or draw
      if valid == True:
      
        #enter a loop that loops back if the user inputs an invalid response
        while played == False:
          PlayDraw = input('Play or Draw?: ').lower()
      
          #if the user inputs play, ask them which card they wish to play
          if PlayDraw == 'play':
            playCard = input('What card would you like to play?: ').upper()
    
            #if the card is not in the user's deck, ask them to input a valid card
            if playCard not in playerDeck and playCard[0] != 'W':
              print('That is an invalid card')
              pDeck = ', '.join(str(x) for x in playerDeck)
              print('Your deck is:', str(pDeck))
              print('The current card on the playing pile is:', face)
              played = False
      
            #check if the card is in the user's deck
            if playCard in playerDeck:
    
              #check if the played card is a wild+4
              if playCard[0] == 'W' and len(playCard) == 3:
                face = wild(playCard)
                plus(playCard)

              #check if the played card is a wild 
              elif playCard[0] == 'W':
                face = wild(playCard)
    
              #otherwise, check if the card is playable
              elif checkValid(playCard):
                face = playCard
                playerDeck.remove(playCard)
                print('You played', playCard, '\n')

                #check if the second character is in the special list
                if playCard[1] in special:
                  print('You played a special card!\n')
                  skip(playCard)
                  rev(playCard)
                  plus(playCard)
                
                print('The current card on the playing pile is:', face)
                pDeck = ', '.join(str(x) for x in playerDeck)
                print('Your deck is:', str(pDeck))
                played = True
      
          #if the user inputs draw, draw a card
          elif PlayDraw == 'draw':
            add = random.choice(deck)
            playerDeck.append(add)
            print('You drew a', add)
            drawnCard(add)
            played = True

          #if the user does not input a valid response, loop back to played
          else:
            print('You did not play or draw! Please try again!')
            played = False
            
      #if user does not have a valid card, force to draw and ask if they want to play or skip
      if not valid:
        print('You do not have a valid card to play')
        add = random.choice(deck)
        playerDeck.append(add)
        print('You drew a', add)
        drawnCard(add)
      turnNum = turnNum + (1*reverse)

      #if the user reaches zero cards, display the winner and ask to play again
      if len(playerDeck) == 0:
        print('You win!')
        gameLoop = False
        playAgain = input('Would you like to play again? (Y/N): ').upper()
        playMore()

    #enter CPU1's turn if currentTurn function returns CPU1
    elif currentTurn() == 'CPU1':
      print("\nIt is CPU1's turn!")
      time.sleep(0.5)
      print("CPU1 has", len(cpu1Deck), "card(s)")
      cpuTurn(cpu1Deck)

      #if CPU1 reaches zero cards, display the winner and ask to play again
      if len(cpu1Deck) == 0:
        print('CPU1 wins!')
        gameLoop = False
        playAgain = input('Would you like to play again? (Y/N): ').upper()
        playMore()

    #enter CPU2's turn if currentTurn function returns CPU2
    elif currentTurn() == 'CPU2':
      print("\nIt is CPU2's turn!")
      time.sleep(0.5)
      print("CPU2 has", len(cpu2Deck), "card(s)")
      cpuTurn(cpu2Deck)

      #if CPU2 reaches zero cards, display the winner and ask to play again
      if len(cpu2Deck) == 0:
        print('CPU2 wins!')
        gameLoop = False
        playAgain = input('Would you like to play again? (Y/N): ').upper()
        playMore()

    #enter CPU3's turn if currentTurn function returns CPU3
    elif currentTurn() == 'CPU3':
      print("\nIt is CPU3's turn!")
      time.sleep(0.5)
      print("CPU3 has", len(cpu3Deck), "card(s)")
      cpuTurn(cpu3Deck)

      #if the CPU3 reaches zero cards, display the winner and ask to play again
      if len(cpu3Deck) == 0:
        print('CPU3 wins!')
        gameLoop = False
        playAgain = input('Would you like to play again? (Y/N): ').upper()
        playMore()
  #make next computer player play a valid card from their deck and tell the user their placed card
