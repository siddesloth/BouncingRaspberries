import pygame, sys, time, random, re

from pygame.locals import *

pygame.init()

infoObject = pygame.display.Info()

display_width = infoObject.current_w
display_height = infoObject.current_h

player_width = 20
player_height = 7

button_width = 120
button_height = 20
score_height = 10
score_width = 100

playerVelocity = 0

foundPV = ""
foundPLV = ""
foundPH = ""
foundPW = ""
foundPC1 = ""
foundPC2 = ""
foundPC3 = ""

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)

hasJumped = False
tickCounter = 0

screen = pygame.display.set_mode((display_width,display_height),0,32)
pygame.display.set_caption('Bouncing Raspberries')

clock = pygame.time.Clock()

backgroundfile = "cloudbackgroundLarge.png"
platformOneFile = "platform2.png"

background = pygame.image.load(backgroundfile).convert() #setting the image to use as the background
platformOne = pygame.image.load(platformOneFile).convert()

playerImg = pygame.image.load('smallLogo.png') #setting the image to use as the player's icon

def player(x,y):
    screen.blit(playerImg, (x,y)) #puts the user's player icon onto the screen

def gameOver():
    text_file = open("HighScores.txt", "a") #opens the high scores file in 'add' mode
    text_file.write("Player's score is: {0} \n".format(getTickCounter())) #writes the score into the file
    text_file.close() #closes the file
    achievedScore = getTickCounter()
    resetTickCounter() #reset game tick for next game
    message_display("Game Over! You scored: {0}".format(achievedScore))
    
def getHighScores():
    hiScores = []
    text_file = open("HighScores.txt", "r") #opens the high scores file in read only mode
    for line in text_file:
        hiScores.append(line) #puts all lines from the file into a list
    return hiScores

def message_display(message):
    textDef = pygame.font.Font('freesansbold.ttf',15)
    TextSurf, TextRect = text_objects(message, textDef)
    TextRect.center = ((display_width/2), (display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(5)

    main_menu()
    
def display_hi_score(score): #a simple function to get the game's current tick and display it as the user's score
    textDef = pygame.font.Font('freesansbold.ttf',10)
    TextSurf, TextRect = text_objects("Score: " + score, textDef)
    TextRect.center = (50,50)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    
def getIfJumped():
    global hasJumped
    return hasJumped #gets and returns if the player has recently jumped

def setIfJumped(jumped):
    global hasJumped
    hasJumped = jumped #sets if the player has recently jumped - used to check if they have 'landed' or not
    
def setTickCounter(counter):
    global tickCounter
    tickCounter += counter #increases the game's tick count
    
def resetTickCounter():
    global tickCounter
    tickCounter = 0 #resets the game's tick count
    
def getTickCounter():
    global tickCounter
    return tickCounter #gets and returns the game's current tick - used for highscore
    
def getPlayerVelocity():
    global playerVelocity
    return playerVelocity #gets and returns the player's current velocity

def setPlayerVelocity(velocity):
    global playerVelocity #using the global playerVelocity variable so that it will impact the game and all other code
    playerVelocity = velocity

#following functions define and draw the four re-usable platforms that are used within the game
def platformOne(platformsX, platformsY, platformsW, platformsH, colour):
    pygame.draw.rect(screen, colour, [platformsX, platformsY, platformsW, platformsH])
    pygame.draw.rect(screen, red, [platformsX, (platformsY - 1), platformsW, (platformsH/5)])

def platformTwo(platformsX, platformsY, platformsW, platformsH, colour):
    pygame.draw.rect(screen, colour, [platformsX, platformsY, platformsW, platformsH])
    pygame.draw.rect(screen, red, [platformsX, (platformsY - 1), platformsW, (platformsH/5)])

def platformThree(platformsX, platformsY, platformsW, platformsH, colour):
    pygame.draw.rect(screen, colour, [platformsX, platformsY, platformsW, platformsH])
    pygame.draw.rect(screen, red, [platformsX, (platformsY - 1), platformsW, (platformsH/5)])
    
def platformFour(platformsX, platformsY, platformsW, platformsH, colour):
    pygame.draw.rect(screen, colour, [platformsX, platformsY, platformsW, platformsH])
    pygame.draw.rect(screen, red, [platformsX, (platformsY - 1), platformsW, (platformsH/5)])
    
def platformFive(platformsX, platformsY, platformsW, platformsH, colour):
    pygame.draw.rect(screen, colour, [platformsX, platformsY, platformsW, platformsH])
    pygame.draw.rect(screen, red, [platformsX, (platformsY - 1), platformsW, (platformsH/5)])
    
def platformSix(platformsX, platformsY, platformsW, platformsH, colour):
    pygame.draw.rect(screen, colour, [platformsX, platformsY, platformsW, platformsH])
    pygame.draw.rect(screen, red, [platformsX, (platformsY - 1), platformsW, (platformsH/5)])
    
#creates the beginning platform that the user stands on
def startingPlatform(platformsX, platformsY, platformsW, platformsH, colour):
    pygame.draw.rect(screen, colour, [platformsX, platformsY, platformsW, platformsH])
    pygame.draw.rect(screen, colour, [platformsX, (platformsY - 10), platformsW, (platformsH/5)])

#used to create all 'buttons' and other rectangles to display text on
def menuButtons(playX, playY, playW, playH, colour):
    pygame.draw.rect(screen, colour, [playX, playY, playW, playH])

#used to create text to display on screen
def text_objects(message, textDef):
    textSurface = textDef.render(message, True, black)
    return textSurface, textSurface.get_rect()

def learn_the_code():
    learnTheCode = True
    screen.blit(background, (0,0))
    codeImages = ["Screenshot_1", "Screenshot_1", "Screenshot_2", "Screenshot_3", "Screenshot_4", "Screenshot_5", "Screenshot_6", "Screenshot_7", "Screenshot_8", "Screenshot_9", "Screenshot_10", "Screenshot_11", "Screenshot_12", "Screenshot_13", "Screenshot_14", "Screenshot_15", "Screenshot_16", "Screenshot_17"]
    imageToDisplay = 0 #sets which image will be shown
    while learnTheCode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    main_menu()
                if event.key == pygame.K_RIGHT:
                    if imageToDisplay < 17:
                        screen.blit(background, (0,0))
                        imageToDisplay += 1 #changes the image displayed to the next one
                    else:
                        coding_Choice()
                if event.key == pygame.K_LEFT:
                    if imageToDisplay != 0:
                        screen.blit(background, (0,0))
                        imageToDisplay -= 1 #changes the image displayed to the previous one
                    else:
                        coding_Choice() #returns to main menu if on first image
                if event.key == pygame.K_q:
                    pygame.quit()
        codeURL = codeImages[imageToDisplay] + ".png"
        codeFile = codeURL
        code = pygame.image.load(codeFile).convert()
        screen.blit(code, (10,10))
        pygame.display.update()

#Getters and setters
def setFoundPlayerVelocity(PV):
    global foundPV
    foundPV = PV
    
def getFoundPlayerVelocity():
    global foundPV
    return foundPV

def setFoundPlatformVelocity(PLV):
    global foundPLV
    foundPLV = PLV
    
def getFoundPlatformVelocity():
    global foundPLV
    return foundPLV

def setFoundPlatformWidth(PW):
    global foundPW
    foundPW = PW
    
def getFoundPlatformWidth():
    global foundPW
    return foundPW

def setFoundPlatformHeight(PH):
    global foundPH
    foundPH = PH
    
def getFoundPlatformHeight():
    global foundPH
    return foundPH

def setFoundPlatformColour1(PC):
    global foundPC1
    foundPC1 = PC
    
def getFoundPlatformColour1():
    global foundPC1
    return foundPC1

def setFoundPlatformColour2(PC):
    global foundPC2
    foundPC2 = PC
    
def getFoundPlatformColour2():
    global foundPC2
    return foundPC2

def setFoundPlatformColour3(PC):
    global foundPC3
    foundPC3 = PC
    
def getFoundPlatformColour3():
    global foundPC3
    return foundPC3

def saveFileVariables():
    PV = getFoundPlayerVelocity()
    PLV = getFoundPlatformVelocity()
    PW = getFoundPlatformWidth()
    PH = getFoundPlatformHeight()
    PC1 = getFoundPlatformColour1()
    PC2 = getFoundPlatformColour2()
    PC3 = getFoundPlatformColour3()
    
    variable_file = open("variablesForRasp.txt", "w")
    variable_file.write("{0},".format(PV))
    variable_file.write("{0},".format(PLV))
    variable_file.write("{0},".format(PW))
    variable_file.write("{0},".format(PH))
    variable_file.write("{0},".format(PC1))
    variable_file.write("{0},".format(PC2))
    variable_file.write("{0}".format(PC3))
    variable_file.close()
    main_menu()

def setupFileVariables():
    
    with open('variablesForRasp.txt', 'r') as myfile:
        variables = myfile.read()
    allVariables = variables.split(",")
        
    setFoundPlayerVelocity(allVariables[0])
    setFoundPlatformVelocity(allVariables[1])
    setFoundPlatformWidth(allVariables[2])
    setFoundPlatformHeight(allVariables[3])
    setFoundPlatformColour1(allVariables[4])
    setFoundPlatformColour2(allVariables[5])
    setFoundPlatformColour3(allVariables[6])
    change_the_code()

def change_the_code():
    
    changingCode = True
    
    screen.blit(background, (0,0))
    
    while changingCode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    main_menu()
                if event.key == pygame.K_h:
                    changePlatformHeight()
                if event.key == pygame.K_w:
                    changePlatformWidth()
                if event.key == pygame.K_p:
                    changePlayerVelocity()
                if event.key == pygame.K_v:
                    changePlatformVelocity()
                if event.key == pygame.K_c:
                    changePlatformColour()
                if event.key == pygame.K_s:
                    saveFileVariables()
                if event.key == pygame.K_q:
                    pygame.quit()
        textDef = pygame.font.Font('freesansbold.ttf',9)
        TextSurf1, TextRect1 = text_objects("Change Platform (H)eight", textDef) #setting up the text to go onto the six 'code buttons'
        TextSurf2, TextRect2 = text_objects("Change Platform (W)idth", textDef)
        TextSurf3, TextRect3 = text_objects("Change (P)layer Velocity", textDef)
        TextSurf4, TextRect4 = text_objects("Change Platform (V)elocity", textDef)
        TextSurf5, TextRect5 = text_objects("Change Platform (C)olour", textDef)
        TextSurf6, TextRect6 = text_objects("(S)ave and Exit", textDef)
            
        #Following code defines the layout, size and colour of the 'buttons' and their associated text
        menuButtons(((display_width/2) - (button_width/2)), (((display_height - (display_height/6) * 6)) + button_height), button_width, button_height, green)
        TextRect1.center = (((display_width/2)), (button_height + (button_height/2)))
            
        menuButtons(((display_width/2) - (button_width/2)), (((display_height - (display_height/6) * 5)) + button_height), button_width, button_height, yellow)
        TextRect2.center = (((display_width/2)), (button_height + (button_height/2) + ((display_height/6) * 1)))
            
        menuButtons(((display_width/2) - (button_width/2)), (((display_height - (display_height/6) * 4)) + button_height), button_width, button_height, white)
        TextRect3.center = (((display_width/2)), (button_height + (button_height/2) + ((display_height/6) * 2)))
            
        menuButtons(((display_width/2) - (button_width/2)), (((display_height - (display_height/6) * 3)) + button_height), button_width, button_height, yellow)
        TextRect4.center = (((display_width/2)), (button_height + (button_height/2) + ((display_height/6) * 3)))
        
        menuButtons(((display_width/2) - (button_width/2)), (((display_height - (display_height/6) * 2)) + button_height), button_width, button_height, green)
        TextRect5.center = (((display_width/2)), (button_height + (button_height/2) + ((display_height/6) * 4)))
        
        menuButtons((display_width/18), (display_height - 79), score_width, score_height, red)
        TextRect6.center = (((display_width/12) + (score_width/4)), (display_height - 80) + (score_height/2))
        
        #adds all text to screen for above code
        screen.blit(TextSurf1, TextRect1)
        screen.blit(TextSurf2, TextRect2)
        screen.blit(TextSurf3, TextRect3)
        screen.blit(TextSurf4, TextRect4)
        screen.blit(TextSurf5, TextRect5)
        screen.blit(TextSurf6, TextRect6)
        
        pygame.display.update()

def changePlatformHeight():
    height = ""
    userInput = True
    font = pygame.font.Font(None, 15)
    while userInput:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    try:
                        int(float(height))
                        setFoundPlatformHeight(height)
                        change_the_code()
                    except:
                        textDef = pygame.font.Font('freesansbold.ttf',20)
                        TextSurf, TextRect = text_objects("Format for height incorrect, only use numbers with no spaces and/or symbols", textDef)
                        TextRect.center = ((display_width/2), ((display_height/2 + 100)))
                        screen.blit(TextSurf, TextRect)
                        
                        pygame.display.update()
                        time.sleep(3)
                        
                        changePlatformHeight()
                    height = ""
                elif event.unicode.isalpha() == False:
                    height += event.unicode
                elif event.key == K_BACKSPACE:
                    height = height[:-1]
        screen.blit(background, (0,0))
        block = font.render(height, True, black)
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.update()
    
def changePlatformWidth():
    width = ""
    userInput = True
    font = pygame.font.Font(None, 15)
    while userInput:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    try:
                        int(float(width))
                        setFoundPlatformWidth(width)
                        change_the_code()
                    except:
                        textDef = pygame.font.Font('freesansbold.ttf',20)
                        TextSurf, TextRect = text_objects("Format for width incorrect, only use numbers with no spaces and/or symbols", textDef)
                        TextRect.center = ((display_width/2), ((display_height/2 + 100)))
                        screen.blit(TextSurf, TextRect)
                        
                        pygame.display.update()
                        time.sleep(3)
                        
                        changePlatformWidth()
                    width = ""
                elif event.unicode.isalpha() == False:
                    width += event.unicode
                elif event.key == K_BACKSPACE:
                    width = width[:-1]
        screen.blit(background, (0,0))
        block = font.render(width, True, black)
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.update()
    
def changePlayerVelocity():
    PV = ""
    userInput = True
    font = pygame.font.Font(None, 15)
    while userInput:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    try:
                        int(float(PV))
                        setFoundPlayerVelocity(PV)
                        change_the_code()
                    except:
                        textDef = pygame.font.Font('freesansbold.ttf',20)
                        TextSurf, TextRect = text_objects("Format for player velocity incorrect, only use numbers with no spaces and/or symbols", textDef)
                        TextRect.center = ((display_width/2), ((display_height/2 + 100)))
                        screen.blit(TextSurf, TextRect)
                        
                        pygame.display.update()
                        time.sleep(3)
                        
                        changePlayerVelocity()
                    PV = ""
                elif event.unicode.isalpha() == False:
                    PV += event.unicode
                elif event.key == K_BACKSPACE:
                    PV = PV[:-1]
        screen.blit(background, (0,0))
        block = font.render(PV, True, black)
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.update()
    
def changePlatformVelocity():
    PV = ""
    userInput = True
    font = pygame.font.Font(None, 15)
    while userInput:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    try:
                        int(float(PV))
                        setFoundPlatformVelocity(PV)
                        change_the_code()
                    except:
                        textDef = pygame.font.Font('freesansbold.ttf',20)
                        TextSurf, TextRect = text_objects("Format for platform velocity incorrect, only use numbers with no spaces and/or symbols", textDef)
                        TextRect.center = ((display_width/2), ((display_height/2 + 100)))
                        screen.blit(TextSurf, TextRect)
                        
                        pygame.display.update()
                        time.sleep(3)
                        
                        changePlatformVelocity()
                    PV = ""
                elif event.unicode.isalpha() == False:
                    PV += event.unicode
                elif event.key == K_BACKSPACE:
                    PV = PV[:-1]
        screen.blit(background, (0,0))
        block = font.render(PV, True, black)
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.update()
    
def changePlatformColour():
    colour = ""
    userInput = True
    colourNum = 0
    font = pygame.font.Font(None, 15)
    while userInput:
        if colourNum == 0:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        try:
                            int(float(colour))
                            if int(float(colour)) < 256 and int(float(colour)) >= 0:
                                setFoundPlatformColour1(colour)
                                colourNum = 1
                                colour = ""
                            else:
                                textDef = pygame.font.Font('freesansbold.ttf',20)
                                TextSurf, TextRect = text_objects("Format for colour incorrect, only use numbers between 0 and 255 with no spaces and/or symbols", textDef)
                                TextRect.center = ((display_width/2), ((display_height/2 + 100)))
                                screen.blit(TextSurf, TextRect)
                            
                                pygame.display.update()
                                time.sleep(3)
                            
                                colour = ""
                                colourNum = 0
                        except:
                            textDef = pygame.font.Font('freesansbold.ttf',20)
                            TextSurf, TextRect = text_objects("Format for colour incorrect, only use numbers between 0 and 255 with no spaces and/or symbols", textDef)
                            TextRect.center = ((display_width/2), ((display_height/2 + 100)))
                            screen.blit(TextSurf, TextRect)
                            
                            pygame.display.update()
                            time.sleep(3)
                            
                            colour = ""
                            colourNum = 0
                    elif event.unicode.isalpha() == False:
                        colour += event.unicode
                    elif event.key == K_BACKSPACE:
                        colour = colour[:-1]
            screen.blit(background, (0,0))
            block = font.render(colour, True, black)
            rect = block.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(block, rect)
            pygame.display.update()
        elif colourNum == 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        try:
                            int(float(colour))
                            if int(float(colour)) < 256 and int(float(colour)) >= 0:
                                setFoundPlatformColour2(colour)
                                colourNum = 2
                                colour = ""
                            else:
                                textDef = pygame.font.Font('freesansbold.ttf',20)
                                TextSurf, TextRect = text_objects("Format for colour incorrect, only use numbers between 0 and 255 with no spaces and/or symbols", textDef)
                                TextRect.center = ((display_width/2), ((display_height/2 + 100)))
                                screen.blit(TextSurf, TextRect)
                            
                                pygame.display.update()
                                time.sleep(3)
                            
                                colour = ""
                                colourNum = 1
                        except:
                            textDef = pygame.font.Font('freesansbold.ttf',20)
                            TextSurf, TextRect = text_objects("Format for colour incorrect, only use numbers between 0 and 255 with no spaces and/or symbols", textDef)
                            TextRect.center = ((display_width/2), ((display_height/2 + 100)))
                            screen.blit(TextSurf, TextRect)
                            
                            pygame.display.update()
                            time.sleep(3)
                            
                            colour = ""
                            colourNum = 1
                    elif event.unicode.isalpha() == False:
                        colour += event.unicode
                    elif event.key == K_BACKSPACE:
                        colour = colour[:-1]
            screen.blit(background, (0,0))
            block = font.render(colour, True, black)
            rect = block.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(block, rect)
            pygame.display.update()
        elif colourNum == 2:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        try:
                            int(float(colour))
                            if int(float(colour)) < 256 and int(float(colour)) >= 0:
                                setFoundPlatformColour3(colour)
                                change_the_code()
                            else:
                                textDef = pygame.font.Font('freesansbold.ttf',20)
                                TextSurf, TextRect = text_objects("Format for colour incorrect, only use numbers between 0 and 255 with no spaces and/or symbols", textDef)
                                TextRect.center = ((display_width/2), ((display_height/2 + 100)))
                                screen.blit(TextSurf, TextRect)
                            
                                pygame.display.update()
                                time.sleep(3)
                            
                                colour = ""
                                colourNum = 2
                        except:
                            textDef = pygame.font.Font('freesansbold.ttf',20)
                            TextSurf, TextRect = text_objects("Format for colour incorrect, only use numbers between 0 and 255 with no spaces and/or symbols", textDef)
                            TextRect.center = ((display_width/2), ((display_height/2 + 100)))
                            screen.blit(TextSurf, TextRect)
                            
                            pygame.display.update()
                            time.sleep(3)
                            
                            colour = ""
                            colourNum = 0
                    elif event.unicode.isalpha() == False:
                        colour += event.unicode
                    elif event.key == K_BACKSPACE:
                        colour = colour[:-1]
            screen.blit(background, (0,0))
            block = font.render(colour, True, black)
            rect = block.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(block, rect)
            pygame.display.update()

def coding_Choice():
    
    codingChoice = True
    screen.blit(background, (0,0))
    textDef = pygame.font.Font('freesansbold.ttf',15)
    TextSurf1, TextRect1 = text_objects("(L)earn the code", textDef) #setting up the text to go onto the two 'learn buttons'
    TextSurf2, TextRect2 = text_objects("(C)hange the code", textDef)
    
    #Following code defines the layout, size and colour of the 'buttons' and their associated text
    menuButtons(((display_width/2) - (button_width/2)), (((display_height - (display_height/4) * 3)) + button_height), button_width, button_height, yellow)
    TextRect1.center = (((display_width/2)), (button_height + (button_height/2) + ((display_height/4) * 1)))
        
    menuButtons(((display_width/2) - (button_width/2)), (((display_height - (display_height/4) * 2)) + button_height), button_width, button_height, white)
    TextRect2.center = (((display_width/2)), (button_height + (button_height/2) + ((display_height/4) * 2)))
    
    #adds all text to screen for above code
    screen.blit(TextSurf1, TextRect1)
    screen.blit(TextSurf2, TextRect2)
    
    pygame.display.update() #update the screen to display the new screen
    
    while codingChoice:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    main_menu()
                if event.key == pygame.K_c:
                    setupFileVariables()
                if event.key == pygame.K_l:
                    learn_the_code()
                if event.key == pygame.K_q:
                    pygame.quit()

def high_scores_screen():
    
    hsScreen = True
    hiScores = getHighScores() #uses the getHighScores function to read all current high scores into a list
    numHiScores = []
    sortedScores = []
    lastScore = 0
    
    screen.blit(background, (0,0))
    for item in hiScores:
        score = item.split()
        intScore = score[-1]
        numHiScores.append(int(float(intScore)))
    sortedScores = sorted(numHiScores, key=int, reverse=True)
    screen.blit(background, (0,0))
    textDef = pygame.font.Font('freesansbold.ttf',15)
    
    #TextSurf, TextRect = text_objects("(B)ack", textDef)
    #menuButtons((display_width/12), (display_height - 800), (score_width/2), score_height, yellow)
    #TextRect.center = (((display_width/12) + (score_width/4)), (display_height - 800) + (score_height/2))
    #screen.blit(TextSurf, TextRect)
    
    #Checks the length of the list and will create a rectangle with the score and it's position up to 10 elements within the scores list
    if len(sortedScores)>0:
        TextSurf1, TextRect1 = text_objects("1st: {0}".format(sortedScores[0]), textDef) #text object for 1st place
        menuButtons(((display_width/2) - (score_width/2)), (((display_height - (display_height/10) * 10)) + score_height), score_width, score_height, green) #defining and creating the buttons
        TextRect1.center = (((display_width/2)), (score_height + (score_height/2))) #position of the text
        screen.blit(TextSurf1, TextRect1) #adds to screen
        
    if len(sortedScores)>1:
        TextSurf2, TextRect2 = text_objects("2nd: {0}".format(sortedScores[1]), textDef) #text object for 2nd place
        menuButtons(((display_width/2) - (score_width/2)), (((display_height - (display_height/10) * 9)) + score_height), score_width, score_height, green)
        TextRect2.center = (((display_width/2)), (score_height + (score_height/2) + ((display_height/10) * 1)))
        screen.blit(TextSurf2, TextRect2)
        
    if len(sortedScores)>2:
        TextSurf3, TextRect3 = text_objects("3rd: {0}".format(sortedScores[2]), textDef) #3rd place etc...
        menuButtons(((display_width/2) - (score_width/2)), (((display_height - (display_height/10) * 8)) + score_height), score_width, score_height, green)
        TextRect3.center = (((display_width/2)), (score_height + (score_height/2) + ((display_height/10) * 2)))
        screen.blit(TextSurf3, TextRect3)
        
    if len(sortedScores)>3:
        TextSurf4, TextRect4 = text_objects("4th: {0}".format(sortedScores[3]), textDef)
        menuButtons(((display_width/2) - (score_width/2)), (((display_height - (display_height/10) * 7)) + score_height), score_width, score_height, green)
        TextRect4.center = (((display_width/2)), (score_height + (score_height/2) + ((display_height/10) * 3)))
        screen.blit(TextSurf4, TextRect4)
        
    if len(sortedScores)>4:
        TextSurf5, TextRect5 = text_objects("5th: {0}".format(sortedScores[4]), textDef)
        menuButtons(((display_width/2) - (score_width/2)), (((display_height - (display_height/10) * 6)) + score_height), score_width, score_height, green)
        TextRect5.center = (((display_width/2)), (score_height + (score_height/2) + ((display_height/10) * 4)))
        screen.blit(TextSurf5, TextRect5)
        
    if len(sortedScores)>5:
        TextSurf6, TextRect6 = text_objects("6th: {0}".format(sortedScores[5]), textDef)
        menuButtons(((display_width/2) - (score_width/2)), (((display_height - (display_height/10) * 5)) + score_height), score_width, score_height, green)
        TextRect6.center = (((display_width/2)), (score_height + (score_height/2) + ((display_height/10) * 5)))
        screen.blit(TextSurf6, TextRect6)
        
    if len(sortedScores)>6:
        TextSurf7, TextRect7 = text_objects("7th: {0}".format(sortedScores[6]), textDef)
        menuButtons(((display_width/2) - (score_width/2)), (((display_height - (display_height/10) * 4)) + score_height), score_width, score_height, green)
        TextRect7.center = (((display_width/2)), (score_height + (score_height/2) + ((display_height/10) * 6)))
        screen.blit(TextSurf7, TextRect7)
        
    if len(sortedScores)>7:
        TextSurf8, TextRect8 = text_objects("8th: {0}".format(sortedScores[7]), textDef)
        menuButtons(((display_width/2) - (score_width/2)), (((display_height - (display_height/10) * 3)) + score_height), score_width, score_height, green)
        TextRect8.center = (((display_width/2)), (score_height + (score_height/2) + ((display_height/10) * 7)))
        screen.blit(TextSurf8, TextRect8)
        
    if len(sortedScores)>8:
        TextSurf9, TextRect9 = text_objects("9th: {0}".format(sortedScores[8]), textDef)
        menuButtons(((display_width/2) - (score_width/2)), (((display_height - (display_height/10) * 2)) + score_height), score_width, score_height, green)
        TextRect9.center = (((display_width/2)), (score_height + (score_height/2) + ((display_height/10) * 8)))
        screen.blit(TextSurf9, TextRect9)
        
    if len(sortedScores)>9:
        TextSurf10, TextRect10 = text_objects("10th: {0}".format(sortedScores[9]), textDef)
        menuButtons(((display_width/2) - (score_width/2)), (((display_height - (display_height/10) * 1)) + score_height), score_width, score_height, green)
        TextRect10.center = (((display_width/2)), (score_height + (score_height/2) + ((display_height/10) * 9)))
        screen.blit(TextSurf10, TextRect10)
        
    pygame.display.update() #update screen
    
    while hsScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    main_menu()
                if event.key == pygame.K_q:
                    pygame.quit()
            

def main_menu():
    
    menuScreen =  True
    
    while menuScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: #p key is pressed
                    game_loop() #play the game
                elif event.key == pygame.K_h: #h key is pressed
                    high_scores_screen() #high scores are shown
                elif event.key == pygame.K_l: #l key is pressed
                    coding_Choice()
                elif event.key == pygame.K_q: #q key is pressed
                    pygame.quit() #quits the game
                    
        screen.blit(background, (0,0)) #sets the background
        textDef = pygame.font.Font('freesansbold.ttf',15)
        TextSurf1, TextRect1 = text_objects("(P)lay", textDef) #setting up the text to go onto the four 'menu buttons'
        TextSurf2, TextRect2 = text_objects("(H)igh-scores", textDef)
        TextSurf3, TextRect3 = text_objects("(L)earn to code", textDef)
        TextSurf4, TextRect4 = text_objects("(Q)uit", textDef)
        
        #Following code defines the layout, size and colour of the 'buttons' and their associated text
        menuButtons(((display_width/2) - (button_width/2)), (((display_height - (display_height/4) * 4)) + button_height), button_width, button_height, green)
        TextRect1.center = (((display_width/2)), (button_height + (button_height/2)))
        
        menuButtons(((display_width/2) - (button_width/2)), (((display_height - (display_height/4) * 3)) + button_height), button_width, button_height, yellow)
        TextRect2.center = (((display_width/2)), (button_height + (button_height/2) + ((display_height/4) * 1)))
        
        menuButtons(((display_width/2) - (button_width/2)), (((display_height - (display_height/4) * 2)) + button_height), button_width, button_height, white)
        TextRect3.center = (((display_width/2)), (button_height + (button_height/2) + ((display_height/4) * 2)))
        
        menuButtons(((display_width/2) - (button_width/2)), (((display_height - (display_height/4) * 1)) + button_height), button_width, button_height, red)
        TextRect4.center = (((display_width/2)), (button_height + (button_height/2) + ((display_height/4) * 3)))
        
        #adds all text to screen for above code
        screen.blit(TextSurf1, TextRect1)
        screen.blit(TextSurf2, TextRect2)
        screen.blit(TextSurf3, TextRect3)
        screen.blit(TextSurf4, TextRect4)

        pygame.display.update() #update the game display
        
    
        
def game_loop():
    t = time.time()
    setIfJumped(False)
    
    with open('variablesForRasp.txt', 'r') as myfile:
        variables = myfile.read()
    allVariables = variables.split(",")
        
    setPlayerVelocity(int(float(allVariables[0])))
    x = (display_width * 0.45)
    y = (display_height * 0.6)

    x_change = 0
    y_change = 0
    
    starting_platformX = 0
    starting_platformY = 0

    platform_startX1 = random.randrange(0, display_width) #choosing a random starting location for the platforms - in terms of X
    platform_startX2 = random.randrange(0, display_width) #...
    platform_startX3 = random.randrange(0, display_width)
    platform_startX4 = random.randrange(0, display_width)
    platform_startX5 = random.randrange(0, display_width)
    platform_startX6 = random.randrange(0, display_width)
    platform_startY1 = -50 #choosing how far off the screen the platforms start
    platform_startY2 = -100
    platform_startY3 = -150 
    platform_startY4 = -200
    platform_startY5 = -250
    platform_startY6 = -300 
    platform_speed = int(float(allVariables[1])) #speed at which the platforms 'fall'
    platform_width = int(float(allVariables[2])) #width of platforms
    platform_height = int(float(allVariables[3])) #height of platforms
    starting_platform_height = display_height #starting platform's height

    GameOver = False
    Fps = 60

    while not GameOver:
        
        t1 = time.time()
        display_hi_score(str(getTickCounter())) #displays the user's current score on screen
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                t = t1
                GameOver = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5 #when the left arrow is pressed/held, moves the player 5 units to the left each tick
                elif event.key == pygame.K_RIGHT:
                    x_change = 5 #when the right arrow is pressed/held, moves the player 5 units to the right each tick
                elif event.key == pygame.K_UP:
                    #when the up arrow is pressed/held...
                    if getIfJumped() == False: #if the player has landed since last jump
                        y_change = -15 #moves the player up by 15 units each tick
                        setPlayerVelocity(int(float(allVariables[0]))) #sets fall velocity back to 5
                        setIfJumped(True) #sets user has jumped - can't jump again until landing
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0 #when letting go of the left or right arrow the player will be still again
                elif event.key == pygame.K_UP:
                    y_change = 0 #when letting go of the up arrow the player will stop moving up
                    
        x += x_change #changes x location
        y += y_change #changes y location
                    
        screen.blit(background, (0,0)) #adds background to screen
            
        pygame.mouse.set_visible(False) #hides the mouse
        
        getVelocity = getPlayerVelocity() #gets how fast the player should be falling
        y = y + getVelocity #moves the player down by the velocity variable each tick
        
        startingPlatform(starting_platformX, starting_platformY + display_height, display_width, starting_platform_height, black) #draws starting platform
            
        platColour1 = int(float(allVariables[4])) #gets the user's choice on the RGB pallet to use for the platforms
        platColour2 = int(float(allVariables[5])) #...
        platColour3 = int(float(allVariables[6])) #...
        
        fullPlatColour = (platColour1, platColour2, platColour3)
        #draws all other platforms
        platformOne(platform_startX1, platform_startY1, platform_width, platform_height, fullPlatColour)
        platformTwo(platform_startX2, platform_startY2, platform_width, platform_height, fullPlatColour)
        platformThree(platform_startX3, platform_startY3, platform_width, platform_height, fullPlatColour)
        platformFour(platform_startX4, platform_startY4, platform_width, platform_height, fullPlatColour)
        platformFive(platform_startX5, platform_startY5, platform_width, platform_height, fullPlatColour)
        platformSix(platform_startX6, platform_startY6, platform_width, platform_height, fullPlatColour)
        
        #moves all platforms down the screen via their speed variable
        platform_startY1 += platform_speed
        platform_startY2 += platform_speed
        platform_startY3 += platform_speed
        platform_startY4 += platform_speed
        platform_startY5 += platform_speed
        platform_startY6 += platform_speed
            
        player(x,y) #draws the player
        
        setTickCounter(1) 
        dt = t1 - t
        if dt >= 8: #this is a check to make sure that the player can stand on the starting platform for the first 8 seconds of the game - allows time for platforms to fall
            starting_platformY += platform_speed

        if x  > display_width - player_width or x < 0: #if the player hits the side of the screen, this stops them going any further
            x_change = 0

        if y > display_height - (player_height * 8) or y < 0: #if the player hits the top or bottom of the screen
            if dt >= 8: 
                t = t1
                gameOver()
            else:
                setPlayerVelocity(0)
                setIfJumped(False)

        if platform_startY1 > display_height:
            platform_startY1 = 0 - platform_height
            platform_startX1 = random.randrange(0,display_width)

        if platform_startY2 > display_height:
            platform_startY2 = 0 - platform_height
            platform_startX2 = random.randrange(0,display_width)

        if platform_startY3 > display_height:
            platform_startY3 = 0 - platform_height
            platform_startX3 = random.randrange(0,display_width)
            
        if platform_startY4 > display_height:
            platform_startY4 = 0 - platform_height
            platform_startX4 = random.randrange(0,display_width)
            
        if platform_startY5 > display_height:
            platform_startY5 = 0 - platform_height
            platform_startX5 = random.randrange(0,display_width)
            
        if platform_startY6 > display_height:
            platform_startY6 = 0 - platform_height
            platform_startX6 = random.randrange(0,display_width)
            
        #Start of collision code for platform one
        if y < platform_startY1 + platform_height and y > platform_startY1 - (platform_height + (platform_height/5)):
            if x > platform_startX1 and x < platform_startX1 + platform_width or x + player_width > platform_startX1 and x + player_width < platform_startX1 + platform_width:
                setPlayerVelocity(platform_speed) #when moving off of platform, change velocity back to player velocity
                setIfJumped(False)

        if y < platform_startY1 + platform_height and y > platform_startY1 - platform_height:

            if x > platform_startX1 and x < platform_startX1 + platform_width or x + player_width > platform_startX1 and x + player_width < platform_startX1 + platform_width:
                t = t1
                gameOver()
        #End of collision code for platform one
                
        #Start of collision code for platform two
        if y < platform_startY2 + platform_height and y > platform_startY2 - (platform_height + (platform_height/5)):
            if x > platform_startX2 and x < platform_startX2 + platform_width or x + player_width > platform_startX2 and x + player_width < platform_startX2 + platform_width:
                setPlayerVelocity(platform_speed)
                setIfJumped(False)

        if y < platform_startY2 + platform_height and y > platform_startY2 - platform_height:

            if x > platform_startX2 and x < platform_startX2 + platform_width or x + player_width > platform_startX2 and x + player_width < platform_startX2 + platform_width:
                t = t1
                gameOver()
        #End of collision code for platform two
                
        #Start of collision code for platform three
        if y < platform_startY3 + platform_height and y > platform_startY3 - (platform_height + (platform_height/5)):
            if x > platform_startX3 and x < platform_startX3 + platform_width or x + player_width > platform_startX3 and x + player_width < platform_startX3 + platform_width:
                setPlayerVelocity(platform_speed)
                setIfJumped(False)

        if y < platform_startY3 + platform_height and y > platform_startY3 - platform_height:

            if x > platform_startX3 and x < platform_startX3 + platform_width or x + player_width > platform_startX3 and x + player_width < platform_startX3 + platform_width:
                t = t1
                gameOver()
        #End of collision code for platform three
                
        #Start of collision code for platform four
        if y < platform_startY4 + platform_height and y > platform_startY4 - (platform_height + (platform_height/5)):
            if x > platform_startX4 and x < platform_startX4 + platform_width or x + player_width > platform_startX4 and x + player_width < platform_startX4 + platform_width:
                setPlayerVelocity(platform_speed)
                setIfJumped(False)

        if y < platform_startY4 + platform_height and y > platform_startY4 - platform_height:

            if x > platform_startX4 and x < platform_startX4 + platform_width or x + player_width > platform_startX4 and x + player_width < platform_startX4 + platform_width:
                t = t1
                gameOver()
        #End of collision code for platform four
        
        #Start of collision code for platform five
        if y < platform_startY5 + platform_height and y > platform_startY5 - (platform_height + (platform_height/5)):
            if x > platform_startX5 and x < platform_startX5 + platform_width or x + player_width > platform_startX5 and x + player_width < platform_startX5 + platform_width:
                setPlayerVelocity(platform_speed)
                setIfJumped(False)

        if y < platform_startY5 + platform_height and y > platform_startY5 - platform_height:

            if x > platform_startX5 and x < platform_startX5 + platform_width or x + player_width > platform_startX5 and x + player_width < platform_startX5 + platform_width:
                t = t1
                gameOver()
        #End of collision code for platform five
                
        #Start of collision code for platform six
        if y < platform_startY6 + platform_height and y > platform_startY6 - (platform_height + (platform_height/5)):
            if x > platform_startX6 and x < platform_startX6 + platform_width or x + player_width > platform_startX6 and x + player_width < platform_startX6 + platform_width:
                setPlayerVelocity(platform_speed)
                setIfJumped(False)

        if y < platform_startY6 + platform_height and y > platform_startY6 - platform_height:

            if x > platform_startX6 and x < platform_startX6 + platform_width or x + player_width > platform_startX6 and x + player_width < platform_startX6 + platform_width:
                t = t1
                gameOver()
        #End of collision code for platform six
            
        pygame.display.update()
            
        clock.tick(Fps)
        
main_menu()
pygame.quit()
sys.exit()
