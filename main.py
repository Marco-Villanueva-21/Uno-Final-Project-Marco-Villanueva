import random
import time

deck = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'RS', 'RR', 'R+2', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'BS', 'BR', 'B+2', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'YS', 'YR', 'Y+2', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'GS', 'GR', 'G+2', 'WC', 'W+4']

special = ['S', 'R', '+']
colors = ['R', 'B', 'Y', 'G']

print('Welcome to UNO!')
time.sleep(1)
print('\nThe rules are simple, you have to match the color or number of the card in your hand with the playing pile card and be the first player to get rid of all of your cards.')
time.sleep(1)
print('\nCards with an "S" at the end will skip the next player')
time.sleep(1)
print('Cards with an "R" at the end will reverse the order of the players')
time.sleep(1)
print('Cards with a "W" will allow you to pick a color')
time.sleep(1)
print('Cards with a "+2" or "+4" will give the next player 2 or 4 cards if they cannot add on to the +2 or +4')
time.sleep(1)
print('You will be playing against 3 other CPU players! Try to come out on top!')
time.sleep(1)

gameExit = True

#define the play again checker at the end of the game
def playMore():
  global playAgainCheck, playAgain, gameExit

  #enter a loop that loops back when the user inputs an invalid response
  while not playAgainCheck:

    #if the user inputs "Y", reset the game
    if playAgain == 'Y':
      print("Let's play again!")
      playAgainCheck = True
      gameExit = True

    #otherwise, exit the game loop
    elif playAgain == 'N':
      print('\nThanks for playing!')
      playAgainCheck = True
      gameExit = False
      
    else:
      playAgain = False
      
#decide whose turn it currently is
def currentTurn():
  global turnNum

  #when the turn reaches past CPU3, loop back to user
  if turnNum > 3:
    turnNum = 0

  #when the turn goes past the user, loop back to CPU3 (for when a reverse card is played)
  if turnNum < 0:
    turnNum = 3
  playTurn = turn[turnNum]
  return playTurn
  
#function to check if the user's deck has a valid card to play
def checkValid(playCard, face):

  #if the playCard matches the face card or the playCard is a wild card, the card is valid
  if playCard[0] == face[0] or playCard[1] == face[1] or playCard[0] == 'W':
    return True
  else:
    return False

#function for drawing a card
def drawnCard(add, deck):
  global face

  #enter a loop that loops back when the user inputs an invalid response
  validResponse = False
  while not validResponse:
    
    #check if the drawn card is valid
    if checkValid(add, face):
      PD = input('You drew a valid card! Play or skip?: ').lower()
  
      #player asks to play
      if PD == 'play' or PD == 'p':
        face = add

        #check if the drawn card is a wild+4 card
        if add[0] == 'W' and len(add) == 3:
          face = wild(add)
          plus(add, deck)

        #check if the drawn card is a wild card
        elif add[0] == 'W':
          wild(add)

          #check if the second character is in the special list
        elif add[1] in special: 
          print('You played a special card!')
          skip(add, deck)
          rev(add, deck)
          plus(add, deck)

        #basic card is played
        else:
          print('You played', add)
          time.sleep(1)
          print('The current card on the playing pile is:', face)
        validResponse = True
  
      #user asks to skip
      elif PD == 'skip' or PD == 's':
        print('You skipped your turn!')
        validResponse = True

      #tell the user they inputted an invalid response and loop back
      else:
        print('You inputted an invalid response, please try again')
        validResponse = False
  
    #if the card is invalid, skip the player's turn
    else:
      print('You drew an invalid card! You must skip your turn!')
      validResponse = True

#define function to count how many cards of each color the CPU has
def countColor(cpuDeck):
  redCount = 0
  blueCount = 0
  greenCount = 0
  yellowCount = 0

  #go through the CPU's entire deck to search and count colors
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

#define how a CPU will play
def cpuTurn(cpuDeck):
  global turnNum
  global face
  
  playTurn = currentTurn()
  validCards = []
  valid = False
  specialPlayed = False
  
  #check each card in the CPU's deck
  for x in range (0, len(cpuDeck)):
    if checkValid(cpuDeck[0+x], face):
      valid = True
      validCards.append(cpuDeck[0+x])

  #if the CPU has a valid card, check for a special card
  if valid:
    for x in range (0, len(validCards)):
    
      #if a special card is found, play it
      if validCards[0+x][1] in special or validCards[0+x][0] == 'W':

        specialPlayed = True
        cpuWild(validCards[0+x], cpuDeck)
        skip(validCards[0+x], cpuDeck)
        rev(validCards[0+x], cpuDeck)
        plus(validCards[0+x], cpuDeck)
        break

    #check if a special card was not played and play a random card from the validCards list
    if not specialPlayed:
      playCard = random.choice(validCards)
      face = playCard
      cpuDeck.remove(playCard)
      time.sleep(1)
      print(playTurn, 'played', playCard)
      time.sleep(1)
      print('The current card on the playing pile is:', face)

  #if the CPU does not have a valid card, force to draw and play if possible, otherwise skip their turn
  if not valid:
    add = random.choice(deck)
    cpuDeck.append(add)
    time.sleep(1)
    print(playTurn, 'drew a card!')
    drawnCardCPU(add, cpuDeck)
  cpuUNO(cpuDeck, playTurn)
  turnNum = turnNum + (1*reverse)

#have the cpu call UNO when they have one card left
def cpuUNO(cpuDeck, uno):

  if len(cpuDeck) == 1:
    print('\n')
    print(uno, 'has UNO!\n')
  
#define CPU's ability to draw a card
def drawnCardCPU(add, cpuDeck):
  global playTurn
  global turnNum
  global face
  
  playTurn = currentTurn()

  if add[0] == 'W' and add[1] == '+':
    face = cpuWild(add, cpuDeck)
    plus(add, cpuDeck)

  #check if the drawn card is a wild card
  elif add[0] == 'W':
    cpuWild(add, cpuDeck)

  #check if the second character is in the special list and is a valid card
  elif add[1] in special and checkValid(add, face): 
    print(playTurn, 'played a special card!')
    skip(add, cpuDeck)
    rev(add, cpuDeck)
    plus(add, cpuDeck)

  #if a valid card is found, the CPU will play it
  elif checkValid(add, face):
    face = add
    time.sleep(1)
    print(playTurn, 'played', add)
    time.sleep(1)
    cpuDeck.remove(add)
    print('The current card on the playing pile is:', face)

  #otherwise, the CPU will skip their turn
  else:
    time.sleep(1)
    print(playTurn, 'skipped their turn!')
    
#decide how a CPU plays a wild card
def cpuWild(playCard, cpuDeck):
  global turnNum, face, colors
  countedColors = []
  possible = []
  
  playTurn = currentTurn()

  #check if the CPU played a wild card
  if playCard[0] == 'W':

    #if they did, count how many cards of each color they have for the best color to play
    time.sleep(1)
    print(playTurn, 'has played a wild card!')
    redCount, blueCount, greenCount, yellowCount = countColor(cpuDeck)

    #put the counted colors into a list
    countedColors.append(redCount)
    countedColors.append(blueCount)
    countedColors.append(greenCount)
    countedColors.append(yellowCount)

    #find the highest value
    mostColor = max(countedColors)

    #check each color to see if it matches the highest value
    if mostColor == redCount:
      possible.append('R')
    if mostColor == blueCount:
      possible.append('B')
    if mostColor == greenCount:
      possible.append('G')
    if mostColor == yellowCount:
      possible.append('Y')

    #have a 20% chance of picking a random color instead of the most logical color
    fake = random.randint(1, 5)
    if fake == 5:
      chosenColor = random.choice(colors)

    #otherwise, pick a random color between the most ideal colors
    else:
      chosenColor = random.choice(possible)

    face = chosenColor + 'C'

    #remove the card from the player's deck if it is not a W+4
    if playCard[1] != '+':
      cpuDeck.remove(playCard)

    time.sleep(1)
    print(playTurn, 'changed the color to', chosenColor)
    time.sleep(1)
    print('The current card on the playing pile is:', face)
    return face
    
#define wild cards used by user (user can choose a color)
def wild(playCard):
  chooseColor = False

  #check if the playCard is a wild card
  if playCard[0] == 'W':
    
    #wild cards will allow the user to pick a color
    print('You played a Wild Card!')
    while not chooseColor:
      time.sleep(1)
      color = input('What color would you like to change it to? (R, G, B, Y): ').upper()
  
      #if the user inputs a valid color, change the card to that color
      if color in colors:
        face = color + 'C'
        print('You changed the color to', color)
        time.sleep(1)
        print('The current card on the playing pile is:', face)

        #remove the card from the deck if it is not a W+4 
        if playCard[1] != '+':
          playerDeck.remove(playCard)
          
        chooseColor = True
        return face

      #otherwise, tell the user they input an invalid color and loop
      else: 
        print('You picked an invalid color! Type in R, G, B, or Y please')
        chooseColor = False
          
#define skip cards (the next player's turn is skipped)
def skip(playCard, Deck):
  global turnNum, face
  
  playTurn = currentTurn()

  #check if the playCard is a skip card
  if playCard[1] == 'S':

    time.sleep(1)
    print(playTurn, 'played', playCard, 'which is a skip card!')
    face = playCard
    Deck.remove(playCard)

    #skip the next player's turn
    turnNum = turnNum + (reverse*1)
    playTurn = currentTurn()
    time.sleep(1)
    print(playTurn, 'had their turn skipped!')

#define reverse cards (the order of the players reverse)
def rev(playCard, Deck):
  global reverse, face
  playTurn = currentTurn()

  #check if the playCard is a reverse card
  if playCard[1] == 'R':

    #reverse the order of players
    reverse = reverse*(-1)
    time.sleep(1)
    print(playTurn, 'played', playCard, 'which is a reverse card!')
    face = playCard
    Deck.remove(playCard)
    time.sleep(1)
    print('The order of the players has been reversed!')

#define plus cards (2 or 4 cards are forced to be added to the next player's deck and the next player's turn is skipped)
def plus(playCard, Deck):
  global turnNum, reverse, forceDraw, face

  playTurn = currentTurn()

  #check if the playCard is a plus card
  if playCard[1] == '+':
    defended = True
    forceDraw = int(playCard[2])
    Deck.remove(playCard)
    time.sleep(1)
    print(playTurn, 'played', playCard, 'which is a plus card!')

    #loop back when a player has successfully defended a plus card
    while defended:
      plusDetected = False
      face = playCard
  
      #change to next player's turn to see who gets hit with a plus card
      turnNum = turnNum + (reverse*1)
  
      #user is hit
      if currentTurn() == 'User':
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
            time.sleep(1)
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
                time.sleep(0.25)
              print('You drew', forceDraw, 'cards!')
              defended = False

            #loop back if the user inputs an invalid response
            else:
              print('\n')
              print('That is not a valid response! Please type either "defend" or "draw")')
              validResponse = False

        #force the user to draw and skip their turn if a plus card is not found
        else:
          time.sleep(1)
          print('\nYou don\'t have a plus card! You must draw and skip your turn!')
          for x in range(0, forceDraw):
            cDeck = random.choice(deck)
            playerDeck.append(cDeck)
            defended = False
            print('You drew', cDeck)
            time.sleep(0.25)
          print('\nYou drew', forceDraw, 'cards in total! Yikes!')
          
      #CPU1 is hit
      if defended and currentTurn() == 'CPU1':
          cpu1Defended = cpuDefend(cpu1Deck)

          #if CPU1 fails to defend, force to draw and skip their turn
          if not cpu1Defended:
            time.sleep(1)
            for x in range(0,forceDraw):
              cDeck = random.choice(deck)
              cpu1Deck.append(cDeck)
            defended = False
            print('\nCPU1 drew', forceDraw, 'cards!')
            time.sleep(1)
            print("CPU1 has", len(cpu1Deck), "card(s)")
    
      #CPU2 is hit
      if defended and currentTurn() == 'CPU2':
          cpu2Defended = cpuDefend(cpu2Deck)

          #if CPU2 fails to defend, force to draw and skip their turn
          if not cpu2Defended:
            time.sleep(1)
            for x in range(0,forceDraw):
              cDeck = random.choice(deck)
              cpu2Deck.append(cDeck)
            defended = False
            print('\nCPU2 drew', forceDraw, 'cards!')
            time.sleep(1)
            print("CPU2 has", len(cpu2Deck), "card(s)")
  
      #CPU3 is hit
      if defended and currentTurn() == 'CPU3':
          cpu3Defended = cpuDefend(cpu3Deck)

          #if CPU3 fails to defend, force to draw and skip their turn
          if not cpu3Defended:
            time.sleep(1)
            for x in range(0,forceDraw):
              cDeck = random.choice(deck)
              cpu3Deck.append(cDeck)
            defended = False
            print('\nCPU3 drew', forceDraw, 'cards!')
            time.sleep(1)
            print("CPU3 has", len(cpu3Deck), "card(s)")

    #tell the user whose turn was skipped
    playTurn = currentTurn()
    print(playTurn, 'had their turn skipped!')

#define a function for CPU players to defend a plus card
def cpuDefend(cpuDeck):
  global forceDraw, turnNum, face, defended
  
  playTurn = currentTurn()

  #go through each card in the CPU's deck
  for x in range(0, len(cpuDeck)):
    
    #play the first plus card found if possible
    if '+' in cpuDeck[0+x][1]:
      time.sleep(1)
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
while gameExit:
  
  #define variables
  playerDeck = []
  cpu1Deck = []
  cpu2Deck = []
  cpu3Deck = []
  cpuDeck = []
  turn = ['User', 'CPU1', 'CPU2', 'CPU3']
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
  time.sleep(1)
  print(str(pDeck))

  #tell user what card is on top of the playing pile

  face = str(random.choice(deck))

  #if the face card is a wild card, pick another random card until it is not wild
  while face[0] == 'W':
    face = str(random.choice(deck))
  
  while gameLoop:

    #it is the user's turn
    if currentTurn() == 'User':
      played = False
      valid = False

      #tell the user it is their turn, their deck and the playing pile
      pDeck = ', '.join(str(x) for x in playerDeck)
      print('\nIt is your turn!')
      time.sleep(1)
      print('Your deck is:', pDeck)
      time.sleep(1)
      print('The current card on the playing pile is:', face)
      
      #check each card in the user's deck
      for x in range (0, len(playerDeck)):
        if checkValid(playerDeck[0+x], face):
          valid = True
          
      #if the user has a valid card, ask if they wish to play or draw
      if valid:
      
        #enter a loop that loops back if the user inputs an invalid response
        while not played:
          playDraw = input('\nPlay or Draw?: ').lower()
      
          #if the user inputs play, ask them which card they wish to play
          if playDraw == 'play' or playDraw == 'p':
            playCard = input('What card would you like to play?: ').upper()
    
            #if the card is not in the user's deck, ask them to input a valid card
            if playCard not in playerDeck:
              print('\nThat is not a card in your deck!')
              pDeck = ', '.join(str(x) for x in playerDeck)
              time.sleep(1)
              print('Your deck is:', str(pDeck))
              time.sleep(1)
              print('The current card on the playing pile is:', face)
              played = False

            #if the card is not a valid card, ask them to input a valid card
            elif not checkValid(playCard, face) and playCard[0] != 'W':
              print('\nThat is an invalid card!')
              pDeck = ', '.join(str(x) for x in playerDeck)
              time.sleep(1)
              print('Your deck is:', str(pDeck))
              time.sleep(1)
              print('The current card on the playing pile is:', face)
              played = False
      
            #check if the card is in the user's deck
            if playCard in playerDeck:
    
              #check if the played card is a wild+4
              if playCard[0] == 'W' and len(playCard) == 3:
                face = wild(playCard)
                plus(playCard, playerDeck)
                played = True

              #check if the played card is a wild 
              elif playCard[0] == 'W':
                face = wild(playCard)
                played = True
    
              #otherwise, check if the card is playable
              elif checkValid(playCard, face):
                face = playCard
                print('You played', playCard, '\n')

                #check if the second character is in the special list
                if playCard[1] in special:
                  print('You played a special card!\n')
                  skip(playCard, playerDeck)
                  rev(playCard, playerDeck)
                  plus(playCard, playerDeck)

                #if the played card is a basic card, remove from deck
                if playCard[1] not in special:
                  playerDeck.remove(playCard)

                #tell the user the playing pile and their deck
                time.sleep(1)
                print('The current card on the playing pile is:', face)
                pDeck = ', '.join(str(x) for x in playerDeck)
                time.sleep(1)
                print('Your deck is:', str(pDeck))
                played = True
      
          #if the user inputs draw, draw a card
          elif playDraw == 'draw' or playDraw == 'd':
            add = random.choice(deck)
            playerDeck.append(add)
            print('You drew a', add)
            drawnCard(add, playerDeck)
            played = True

          #if the user does not input a valid response, loop back to played
          else:
            print('You did not play or draw! Type in either "play" or "draw"!')
            played = False
            
      #if user does not have a valid card, force to draw and ask if they want to play or skip
      if not valid:
        print('You do not have a valid card to play')
        add = random.choice(deck)
        playerDeck.append(add)
        time.sleep(1)
        print('You drew a', add)
        drawnCard(add, playerDeck)
      turnNum = turnNum + (1*reverse)

      #if the user has one card left, tell them they have UNO 
      if len(playerDeck) == 1:
        print('\nYou have UNO!\n')
      
      #if the user reaches zero cards, display the winner and ask to play again
      if len(playerDeck) == 0:
        print('You win!')
        gameLoop = False
        time.sleep(1)
        playAgain = input('Would you like to play again? (Y/N): ').upper()
        playMore()

    #enter CPU1's turn if currentTurn function returns CPU1
    elif currentTurn() == 'CPU1':
      print("\nIt is CPU1's turn!")
      time.sleep(1)
      print("CPU1 has", len(cpu1Deck), "card(s)")
      cpuTurn(cpu1Deck)

      #if CPU1 reaches zero cards, display the winner and ask to play again
      if len(cpu1Deck) == 0:
        print('CPU1 wins!')
        gameLoop = False
        time.sleep(1)
        playAgain = input('Would you like to play again? (Y/N): ').upper()
        playMore()

    #enter CPU2's turn if currentTurn function returns CPU2
    elif currentTurn() == 'CPU2':
      time.sleep(1)
      print("\nIt is CPU2's turn!")
      print("CPU2 has", len(cpu2Deck), "card(s)")
      cpuTurn(cpu2Deck)

      #if CPU2 reaches zero cards, display the winner and ask to play again
      if len(cpu2Deck) == 0:
        print('CPU2 wins!')
        gameLoop = False
        time.sleep(1)
        playAgain = input('Would you like to play again? (Y/N): ').upper()
        playMore()

    #enter CPU3's turn if currentTurn function returns CPU3
    elif currentTurn() == 'CPU3':
      time.sleep(1)
      print("\nIt is CPU3's turn!")
      print("CPU3 has", len(cpu3Deck), "card(s)")
      cpuTurn(cpu3Deck)

      #if the CPU3 reaches zero cards, display the winner and ask to play again
      if len(cpu3Deck) == 0:
        print('CPU3 wins!')
        gameLoop = False
        time.sleep(1)
        playAgain = input('Would you like to play again? (Y/N): ').upper()
        playMore()