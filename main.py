import pygame, random, math

WIDTH, HEIGHT = (1280, 720)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

def init():
    States()
    initColours()
    initFonts()
    loadAssetsandSettings()
    initLevel1()
    initObjectives()
    initPositions()

def States(): #initialzes the states
    global gameState, TITLE, START, NEXT_LEVEL, GAME_OVER, WIN, QUIT
    TITLE = 0
    START = 1
    NEXT_LEVEL = 2
    GAME_OVER = 3
    WIN = 4
    QUIT = 55
    gameState = TITLE

def initColours(): #initialzes colours
    global BLACK, WHITE, GREY, RED, GREEN, BLUE, PURPLE
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (128, 128, 128)
    RED = (0, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    PURPLE = (76, 0, 153)

def initFonts(): #initialzes the fonts
    global titleFont, enterFont, font
    titleFont = (pygame.font.SysFont(None, 110))
    enterFont = (pygame.font.SysFont(None, 30))
    font = (pygame.font.SysFont(None, 50))

def loadAssetsandSettings(): #loads all images
    global wallBlock, characterBlock, enemyBlock, keyBlock, deathBlock, jailBlock, checkeredBlock, doorClosedBlock, doorOpenBlock
    global switchBlock, powerBlock, playButton, exitButton, powerUpBlock, lives, levels, deathTimer, slowModeTimer, lives
    wallBlock = pygame.image.load("wallblock.png").convert_alpha()
    characterBlock = []
    enemyBlock = []
    keyBlock = pygame.image.load("Keyblock.png").convert_alpha()
    deathBlock = pygame.image.load("deathblock.png")
    jailBlock = pygame.image.load("jailblock.png").convert_alpha()
    checkeredBlock = pygame.image.load("checkeredblock.png")
    doorClosedBlock = pygame.image.load("doorclosedblock.png").convert_alpha()
    doorOpenBlock = pygame.image.load("dooropenblock.png").convert_alpha()
    switchBlock = pygame.image.load("button.png").convert_alpha()
    playButton = pygame.image.load("playbutton.png")
    exitButton = pygame.image.load("exitbutton.png")
    powerBlock = pygame.image.load("powerblock.png").convert_alpha()
    initSounds()

    for i in range(1, 5):
        character = "character" + str(i) + ".png"
        characterBlock.append(pygame.image.load(character))

    for i in range(1, 4):
        enemy = "ghost" + str(i) + ".png"
        enemyBlock.append(pygame.image.load(enemy))
    levels, deathTimer, slowModeTimer, lives = 1, -1, -1, 3


def initSounds():
    global objectiveCompleteSound, countdownSound, deathSound, bloodSound, levelCompleteSound, liveLostSound
    global playerMovementSound, keysDoneSound, keyPickedUpSound, switchFinishedSound, switchesCompletedSound, powerUpSound
    global powerUpUsedSound, countdownSoundPlayed
    objectiveCompleteSound = pygame.mixer.Sound("completion_8_ian.wav")
    countdownSound = pygame.mixer.Sound("miscellaneous_9_ian.wav")
    deathSound = pygame.mixer.Sound("shouting_2_ian.wav")
    bloodSound = pygame.mixer.Sound("mixkit-game-blood-pop-slide-2363.wav")
    levelCompleteSound = pygame.mixer.Sound("mixkit-completion-of-a-level-2063.wav")
    liveLostSound = pygame.mixer.Sound("mixkit-player-losing-or-failing-2042.wav")
    playerMovementSound = pygame.mixer.Sound("mixkit-quick-jump-arcade-game-239.wav")
    keysDoneSound = pygame.mixer.Sound("mixkit-extra-bonus-in-a-video-game-2045.wav")
    keyPickedUpSound = pygame.mixer.Sound("mixkit-video-game-treasure-2066.wav")
    switchFinishedSound = pygame.mixer.Sound("mixkit-arcade-retro-changing-tab-206.wav")
    switchesCompletedSound = pygame.mixer.Sound("mixkit-unlock-game-notification-253.wav")
    countdownSoundPlayed = False

def initLevel1(): #level 1 grid
    global grid, gridPos, BLOCKX_SPACING, BLOCKY_SPACING, totalRows, totalCols, timer, countdownTimer, powerUpTime
    grid = []
    with open("level1.txt", 'r') as fh:  # opens the file and the variable fh (file handler) points to the first line
        for line in fh:
            row = []
            for char in line.strip():
                row.append(char)
            grid.append(row)
    gridPos = (200, 440)
    BLOCKX_SPACING, BLOCKY_SPACING = 35, 35
    totalRows = len(grid)
    totalCols = len(grid[0])
    timer = 0
    countdownTimer = 60


def initLevel2(): #level 2 grid
    global grid, gridPos, BLOCKX_SPACING, BLOCKY_SPACING, totalRows, totalCols, timer, countdownTimer, powerUpTime
    grid = []
    with open("level2.txt", 'r') as fh:  # opens the file and the variable fh (file handler) points to the first line
        for line in fh:
            row = []
            for char in line.strip():
                row.append(char)
            grid.append(row)
    gridPos = (100, 200)
    BLOCKX_SPACING, BLOCKY_SPACING = 35, 35
    totalRows = len(grid)
    totalCols = len(grid[0])
    timer = 0
    countdownTimer = 90

def initLevel3(): #level 3 grid
    global grid, gridPos, BLOCKX_SPACING, BLOCKY_SPACING, totalRows, totalCols, timer, countdownTimer, powerUpTime
    grid = []
    with open("level3.txt", 'r') as fh:  # opens the file and the variable fh (file handler) points to the first line
        for line in fh:
            row = []
            for char in line.strip():
                row.append(char)
            grid.append(row)
    gridPos = (75, 100)
    BLOCKX_SPACING, BLOCKY_SPACING = 35, 35
    totalRows = len(grid)
    totalCols = len(grid[0])
    timer = 0
    countdownTimer = 120

def initObjectives(): #objects positions
    global key1X, key1Y, key2X, key2Y, key3X, key3Y, key1PickedUp, key2PickedUp, key3PickedUp, numKeysPickedUp
    global switch1Connected, switch2Connected, switch3Connected, numSwitchesCompleted, switchesCompleted
    global powerUpX, powerUpY, powerUp, timeIndex, powerUpIndex, escapeRope, doorOpened, powerOn
    key1X = random.randint(1, len(grid) - 1)
    key1Y = random.randint(1, len(grid[0]) - 1)
    key2X = random.randint(1, len(grid) - 1)
    key2Y = random.randint(1, len(grid[0]) - 1)
    key3X = random.randint(1, len(grid) - 1)
    key3Y = random.randint(1, len(grid[0]) - 1)
    key1PickedUp, key2PickedUp, key3PickedUp = (False, False, False)
    numKeysPickedUp = 0
    switch1Connected, switch2Connected, switch3Connected = (False, False, False)
    numSwitchesCompleted = 0
    switchesCompleted, doorOpened, powerOn = False, False, False

def initPositions(): #initalizes positions from grid and stores them into x y variable
    global charX, charY, charStartX, charStartY, charIndex, enemy1X, enemy1Y, enemyStart1X, enemyStart1Y, enemyNext1X, enemyNext1Y
    global enemy1, enemy2X, enemy2Y, enemyStart2X, enemyStart2Y,  enemyNext2X, enemyNext2Y, enemy2, enemy3X, enemy3Y
    global enemyStart3X, enemyStart3Y, enemyNext3X, enemyNext3Y, enemy3, escapeX, escapeY, doorX, doorY, powerX, powerY
    global switch1X, switch1Y, switch2X, switch2Y, switch3X, switch3Y, wallX, wallY, deathX, deathY, rectY, rectIndex, alphaIndex, exit, dead
    enemy1, enemy2, enemy3 = False, False, False
    enemy1X, enemy1Y, enemy2X, enemy2Y, enemy3X, enemy3Y = 0, 0, 0, 0, 0, 0
    for m in range(totalRows):
        for n in range(totalCols):
            pos = grid[m][n]
            if pos == "C":
                charX, charStartX, charY, charStartY = m, m, n, n
                if m <= totalRows/2:
                    charIndex = 0
                else:
                    charIndex = 3
            if pos == "1":
                enemy1X, enemyStart1X, enemy1Y, enemyStart1Y = m, m, n, n
                enemy1 = True
            if pos == "2":
                enemy2X, enemyStart2X, enemy2Y, enemyStart2Y = m, m ,n, n
                enemy2 = True
            if pos == "3":
                enemy3X, enemyStart3X, enemy3Y, enemyStart3Y = m, m, n, n
                enemy3 = True
            if pos == "E":
                escapeX, escapeY = m, n
            if pos == "D":
                doorX, doorY = m, n
            if pos == "P":
                powerX, powerY = m, n
            if pos == "!":
                switch1X, switch1Y = m, n
            if pos == "@":
                switch2X, switch2Y = m, n
            if pos == "#":
                switch3X, switch3Y = m, n
            if pos == "X":
                wallX, wallY = m, n
    deathX, deathY = 0, 0
    alphaIndex = 0, 0
    rectY = (HEIGHT / 2 + 50), (HEIGHT / 2 + 150)
    rectIndex = 0
    enemyNext1X, enemyNext1Y, enemyNext2X, enemyNext2Y, enemyNext3X, enemyNext3Y = charX, charY, charX, charY, charX, charY
    exit, dead = False, False

def update():
    updateGameConditions()
    if gameState == START:
        updateEnemy()
        updateKey()
        updateEnemyContactKey()
        updateSwitchesandPower()
        updateDeath()
        getWallAlpha(alphaIndex)

def updateGameConditions():
    global gameState, timer, countdownTimer, levels, countdownSoundPlayed
    if gameState == START:
        timer += 1
        if timer % 60 == 0:
            countdownTimer -= 1
        if countdownTimer == 3 and countdownSoundPlayed == False:
            countdownSound.play(0)
            countdownSoundPlayed = True
        if lives == 0 or countdownTimer == 0:
            if gameState == START:
                liveLostSound.play(0)
            gameState = GAME_OVER
        if charX == escapeX and charY == escapeY and exit == True and levels == 3:
            if gameState == START:
                levelCompleteSound.play(0)
            gameState = WIN
    if gameState == START or gameState == NEXT_LEVEL: #handle Next Levels
        if charX == escapeX and charY == escapeY and exit == True and levels == 1:
            if gameState == START:
                levelCompleteSound.play(0)
            gameState = NEXT_LEVEL
            initLevel2()
            initObjectives()
            initPositions()
            levels = 2
        if charX == escapeX and charY == escapeY and exit == True and levels == 2:
            if gameState == START:
                levelCompleteSound.play(0)
            gameState = NEXT_LEVEL
            initLevel3()
            initObjectives()
            initPositions()
            levels = 3


def updateEnemy():
    global enemy1X, enemy1Y, enemy2X, enemy2Y, enemy3X, enemy3Y

    speed = 0.02  # Movement speed

    if not dead:
        for enemyX, enemyY in [(enemy1X, enemy1Y), (enemy2X, enemy2Y), (enemy3X, enemy3Y)]:
            diffX = charX - enemyX
            diffY = charY - enemyY
            if diffX == 0 and diffY == 0:
                continue
            if abs(diffX) > abs(diffY):
                if diffX > 0:
                    enemyX += speed
                else:
                    enemyX -= speed
            else:
                if diffY > 0:
                    enemyY += speed
                else:
                    enemyY -= speed
            enemy1X, enemy1Y = enemyX, enemyY
            enemy2X, enemy2Y = enemyX, enemyY
            enemy3X, enemy3Y = enemyX, enemyY

def updateKey():
    global key1PickedUp, key2PickedUp, key3PickedUp, numKeysPickedUp, key1X, key1Y, key2X, key2Y, key3X, key3Y, doorOpened
    if charX == key1X and charY == key1Y and key1PickedUp == False:
        numKeysPickedUp += 1
        keyPickedUpSound.play(0)
        key1PickedUp = True
    if charX == key2X and charY == key2Y and key2PickedUp == False:
        numKeysPickedUp += 1
        keyPickedUpSound.play(0)
        key2PickedUp = True
    if charX == key3X and charY == key3Y and key3PickedUp == False:
        numKeysPickedUp += 1
        keyPickedUpSound.play(0)
        key3PickedUp = True
    if key1PickedUp == True and key2PickedUp == True and key3PickedUp == True and doorOpened != True:
        numKeysPickedUp = 3
        keysDoneSound.play(0)
        doorOpened = True
    while grid[key1X][key1Y] != "_":
        key1X = random.randint(1, len(grid) - 1)
        key1Y = random.randint(1, len(grid[0]) - 1)
    while grid[key2X][key2Y] != "_":
        key2X = random.randint(1, len(grid) - 1)
        key2Y = random.randint(1, len(grid[0]) - 1)
    while grid[key3X][key3Y] != "_":
        key3X = random.randint(1, len(grid) - 1)
        key3Y = random.randint(1, len(grid[0]) - 1)
    while grid[key1X][key1Y] != grid[key2X][key2Y]:
        key1X = random.randint(1, len(grid) - 1)
        key1Y = random.randint(1, len(grid[0]) - 1)
    while grid[key2X][key2Y] != grid[key3X][key3Y]:
        key2X = random.randint(1, len(grid) - 1)
        key2Y = random.randint(1, len(grid[0]) - 1)
    while grid[key3X][key3Y] != grid[key1X][key1Y]:
        key3X = random.randint(1, len(grid) - 1)
        key3Y = random.randint(1, len(grid[0]) - 1)

def updateEnemyContactKey(): #if enemy comes into contact with keys they are repositioned
    global key1X, key1Y, key2X, key2Y, key3X, key3Y
    if enemy1X == key1X and enemy1Y == key1Y:
        key1X = random.randint(1, len(grid) - 1)
        key1Y = random.randint(1, len(grid[0]) - 1)
    if enemy1X == key2X and enemy1Y == key2Y:
        key2X = random.randint(1, len(grid) - 1)
        key2Y = random.randint(1, len(grid[0]) - 1)
    if enemy1X == key3X and enemy1Y == key3Y:
        key3X = random.randint(1, len(grid) - 1)
        key3Y = random.randint(1, len(grid[0]) - 1)
    if enemy2X == key1X and enemy2Y == key1Y:
        key1X = random.randint(1, len(grid) - 1)
        key1Y = random.randint(1, len(grid[0]) - 1)
    if enemy2X == key2X and enemy2Y == key2Y:
        key2X = random.randint(1, len(grid) - 1)
        key2Y = random.randint(1, len(grid[0]) - 1)
    if enemy2X == key3X and enemy2Y == key3Y:
        key3X = random.randint(1, len(grid) - 1)
        key3Y = random.randint(1, len(grid[0]) - 1)
    if enemy3X == key1X and enemy3Y == key1Y:
        key1X = random.randint(1, len(grid) - 1)
        key1Y = random.randint(1, len(grid[0]) - 1)
    if enemy3X == key2X and enemy3Y == key2Y:
        key2X = random.randint(1, len(grid) - 1)
        key2Y = random.randint(1, len(grid[0]) - 1)
    if enemy3X == key3X and enemy3Y == key3Y:
        key3X = random.randint(1, len(grid) - 1)
        key3Y = random.randint(1, len(grid[0]) - 1)

def updateSwitchesandPower(): #switches and power are updated here and kept track
    global switch1Connected, switch2Connected, switch3Connected,numSwitchesCompleted, switchesCompleted, doorOpened, powerOn, exit
    if switch1Connected == True and switch2Connected == True and switch3Connected == True and switchesCompleted == False:
        switchesCompletedSound.play()
        numSwitchesCompleted = 3
        switchesCompleted = True
    if powerOn == True:
        exit = True

def updateDeath(): #if character collides with enemy, everything that happens when dead is here
    global dead, deathX, deathY, charX, charY, enemy1X, enemy1Y, enemy2X, enemy2Y, enemy3X, enemy3Y, lives
    global deathTimer, charIndex, enemyNext1X, enemyNext1Y, enemyNext2X, enemyNext2Y, enemyNext3X, enemyNext3Y
    if round(enemy1X) == charX and round(enemy1Y) == charY:
        deathSound.play(0)
        dead = True
        deathTimer = countdownTimer - 3
        lives -= 1
        bloodSound.play(0)
    elif round(enemy2X) == charX and round(enemy2Y) == charY:
        deathSound.play(0)
        dead = True
        deathTimer = countdownTimer - 3
        lives -= 1
        bloodSound.play(0)
    elif round(enemy3X) == charX and round(enemy3Y) == charY:
        deathSound.play(0)
        dead = True
        deathTimer = countdownTimer - 3
        lives -= 1
        bloodSound.play(0)
    if dead == True:
        deathX, deathY = charX, charY
        if enemy1 == True:
            enemy1X, enemy1Y = enemyStart1X, enemyStart1Y
        if enemy2 == True:
            enemy2X, enemy2Y = enemyStart2X, enemyStart2Y
        if enemy3 == True:
            enemy3X, enemy3Y = enemyStart3X, enemyStart3Y
        if deathTimer == countdownTimer:
            charX, charY = charStartX, charStartY
            if charX <= totalRows / 2:
                charIndex = 0
            else:
                charIndex = 3
            if enemy1 == True:
                enemyNext1X, enemyNext1Y = charX, charY
            if enemy2 == True:
                enemyNext2X, enemyNext2Y = charX, charY
            if enemy3 == True:
                enemyNext3X, enemyNext3Y = charX, charY
            dead = False

def getWallAlpha(alphaIndex): #to change the alpha of the images in game to give a flashlight look
    calc = math.sqrt((alphaIndex[0] - charX) ** 2 + (alphaIndex[1] - charY) ** 2)
    if 2 < calc <= 3:
        return (80)
    elif 1 < calc <= 2:
        return (160)
    elif 0 < calc <= 1:
        return (240)
    else:
        return(0)

def draw():
    '''This function is used to draw things onto the screen'''
    drawBG()
    if gameState == TITLE:
        drawTitle()
    if gameState == NEXT_LEVEL:
        drawNextLevel()
    if gameState == GAME_OVER:
        drawGameOver()
    if gameState == START:
        drawGrid()
        drawEnemy()
        drawAssets()
    if gameState == WIN:
        drawWin()
    pygame.display.flip() #should always be the last line in this function

def drawBG(): #draws background
    pygame.draw.rect(SCREEN, BLACK, (0, 0, WIDTH, HEIGHT))

def drawTitle(): #draws Title Screen
    title = titleFont.render(("GHOST ESCAPE"), True, PURPLE)
    SCREEN.blit(title, (WIDTH/2 - 285, HEIGHT/2 - 125))
    SCREEN.blit(playButton, (WIDTH / 2 - 100, HEIGHT / 2 + 50))
    SCREEN.blit(exitButton, (WIDTH / 2 - 100, HEIGHT / 2 + 150))
    pygame.draw.rect(SCREEN, RED, ((WIDTH / 2 - 100), rectY[rectIndex], 200, 80), 2)
def drawNextLevel(): #draws nextLevel Screen
    title = titleFont.render(("CONGRATULATIONS"), True, BLUE)
    SCREEN.blit(title, (WIDTH/2 - 375, HEIGHT/2 - 90))
    enterMsg = enterFont.render(("Press ENTER To Continue"), True, PURPLE)
    SCREEN.blit(enterMsg, (WIDTH/2 - 140, HEIGHT/2 + 250))

def drawGameOver(): #draws GameOver Screen
    title = titleFont.render(("GAME OVER"), True, RED)
    SCREEN.blit(title, (WIDTH/2 - 240, HEIGHT/2 - 125))
    SCREEN.blit(playButton, (WIDTH / 2 - 100, HEIGHT / 2 + 50))
    SCREEN.blit(exitButton, (WIDTH / 2 - 100, HEIGHT / 2 + 150))
    pygame.draw.rect(SCREEN, RED, ((WIDTH / 2 - 100), rectY[rectIndex], 200, 80), 2)

def drawGrid(): #draws grid onto screen from level text
    global i, j, row, col
    for i in range(totalRows):
        for j in range(totalCols):
            tile = grid[i][j]
            row = gridPos[0] + BLOCKY_SPACING*i
            col = gridPos[1] + BLOCKX_SPACING*j
            drawKeysandDoor()
            drawSwitches()
            if i == escapeX and j == escapeY and exit == False:
                if powerOn == False:
                    alphaIndex = (i, j)
                    alpha = getWallAlpha(alphaIndex)
                    jailBlock.set_alpha(alpha)
                    SCREEN.blit(jailBlock, (col, row))
                else:
                    jailBlock.set_alpha(255)
                    SCREEN.blit(jailBlock, (col, row))
            elif tile == "X":
                if powerOn == False:
                    wallIndex = (i, j)
                    alpha = getWallAlpha(wallIndex)
                    wallBlock.set_alpha(alpha)
                    SCREEN.blit(wallBlock, (col, row))
                else:
                    wallBlock.set_alpha(255)
                    SCREEN.blit(wallBlock, (col, row))
            if i == charX and j == charY and dead == False:
                SCREEN.blit(characterBlock[charIndex], (col, row))
            elif i == deathX and j == deathY and dead == True:
                SCREEN.blit(deathBlock, (col, row))
            elif i == escapeX and j == escapeY and exit == True:
                SCREEN.blit(checkeredBlock, (col, row))
            elif i == powerX and j == powerY and powerOn == False and switchesCompleted == True:
                SCREEN.blit(powerBlock, (col, row))

def drawKeysandDoor():
    if i == key1X and j == key1Y and key1PickedUp == False:
        if powerOn == False:
            alphaIndex = (i, j)
            alpha = getWallAlpha(alphaIndex)
            keyBlock.set_alpha(alpha)
            SCREEN.blit(keyBlock, (col, row))
        else:
            keyBlock.set_alpha(255)
            SCREEN.blit(keyBlock, (col, row))
    elif i == key2X and j == key2Y and key2PickedUp == False:
        if powerOn == False:
            alphaIndex = (i, j)
            alpha = getWallAlpha(alphaIndex)
            keyBlock.set_alpha(alpha)
            SCREEN.blit(keyBlock, (col, row))
        else:
            keyBlock.set_alpha(255)
            SCREEN.blit(keyBlock, (col, row))
    elif i == key3X and j == key3Y and key3PickedUp == False:
        if powerOn == False:
            alphaIndex = (i, j)
            alpha = getWallAlpha(alphaIndex)
            keyBlock.set_alpha(alpha)
            SCREEN.blit(keyBlock, (col, row))
        else:
            keyBlock.set_alpha(255)
            SCREEN.blit(keyBlock, (col, row))
    elif i == doorX and j == doorY and doorOpened == False:
        if powerOn == False:
            alphaIndex = (i, j)
            alpha = getWallAlpha(alphaIndex)
            doorClosedBlock.set_alpha(alpha)
            SCREEN.blit(doorClosedBlock, (col, row))
        else:
            doorClosedBlock.set_alpha(255)
            SCREEN.blit(doorClosedBlock, (col, row))
    elif i == doorX and j == doorY and doorOpened == True:
            SCREEN.blit(doorOpenBlock, (col, row))

def drawSwitches():
    if i == switch1X and j == switch1Y and switch1Connected == False:
        if powerOn == False:
            alphaIndex = (i, j)
            alpha = getWallAlpha(alphaIndex)
            switchBlock.set_alpha(alpha)
            SCREEN.blit(switchBlock, (col, row))
        else:
            switchBlock.set_alpha(255)
            SCREEN.blit(switchBlock, (col, row))
    elif i == switch2X and j == switch2Y and switch2Connected == False:
        if powerOn == False:
            alphaIndex = (i, j)
            alpha = getWallAlpha(alphaIndex)
            switchBlock.set_alpha(alpha)
            SCREEN.blit(switchBlock, (col, row))
        else:
            switchBlock.set_alpha(255)
            SCREEN.blit(switchBlock, (col, row))
    elif i == switch3X and j == switch3Y and switch3Connected == False:
        if powerOn == False:
            alphaIndex = (i, j)
            alpha = getWallAlpha(alphaIndex)
            switchBlock.set_alpha(alpha)
            SCREEN.blit(switchBlock, (col, row))
        else:
            switchBlock.set_alpha(255)
            SCREEN.blit(switchBlock, (col, row))

def drawEnemy():
    if enemy1 == True:
        SCREEN.blit(enemyBlock[0], ((gridPos[1] + BLOCKX_SPACING*enemy1Y), (gridPos[0] + BLOCKY_SPACING*enemy1X)))
    if enemy2 == True:
        SCREEN.blit(enemyBlock[1], ((gridPos[1] + BLOCKX_SPACING*enemy2Y), (gridPos[0] + BLOCKY_SPACING*enemy2X)))
    if enemy3 == True:
        SCREEN.blit(enemyBlock[2], ((gridPos[1] + BLOCKX_SPACING*enemy3Y), (gridPos[0] + BLOCKY_SPACING*enemy3X)))

def drawAssets():
    levelsImg = font.render("Level: " + str(levels), True, WHITE)
    SCREEN.blit(levelsImg, (55, 30))
    livesImg = font.render("Lives: " + str(lives), True, WHITE)
    SCREEN.blit(livesImg, (205, 30))
    countdownTimerImg = font.render("Timer: " + str(countdownTimer), True, WHITE)
    SCREEN.blit(countdownTimerImg, (355, 30))
    keysCompletedImg = font.render("Keys: " + str(numKeysPickedUp) + "/3", True, WHITE)
    SCREEN.blit(keysCompletedImg, (540, 30))
    switchesCompletedImg = font.render("Switch: " + str(numSwitchesCompleted) + "/3", True, WHITE)
    SCREEN.blit(switchesCompletedImg, (705, 30))
    if powerOn == False:
        powerOnImg = font.render("Power: OFF", True, WHITE)
        SCREEN.blit(powerOnImg, (900, 30))
    else:
        powerOnImg = font.render("Power: ON", True, WHITE)
        SCREEN.blit(powerOnImg, (900, 30))

def drawWin():
    title = titleFont.render(("CONGRATULATIONS"), True, BLUE)
    SCREEN.blit(title, (WIDTH / 2 - 375, HEIGHT / 2 - 150))
    title = titleFont.render(("YOU WIN"), True, WHITE)
    SCREEN.blit(title, (WIDTH / 2 - 175, HEIGHT / 2 - 50))
    SCREEN.blit(playButton, (WIDTH / 2 - 100, HEIGHT / 2 + 50))
    SCREEN.blit(exitButton, (WIDTH / 2 - 100, HEIGHT / 2 + 150))
    pygame.draw.rect(SCREEN, RED, ((WIDTH / 2 - 100), rectY[rectIndex], 200, 80), 2)

def playerMovement(): #handles playermovement, called from main
    global grid, charX, charY, charIndex
    keys = pygame.key.get_pressed()
    if dead == False:
        if keys[pygame.K_a] and grid[charX][charY - 1] != "X":
            if grid[charX][charY - 1] != "D" or doorOpened == True:
                if grid[charX][charY - 1] != "E" or exit == True:
                    charIndex = 1
                    nextPos = charY - 1
                    characterPos = grid[charX][charY]
                    grid[charX][charY] = grid[charX][nextPos]
                    grid[charX][nextPos] = characterPos
                    charY = charY - 1
                    playerMovementSound.play(0)
        elif keys[pygame.K_d] and grid[charX][charY + 1] != "X":
            if grid[charX][charY + 1] != "D" or doorOpened == True:
                if grid[charX][charY + 1] != "E" or exit == True:
                    charIndex = 2
                    nextPos = charY + 1
                    characterPos = grid[charX][charY]
                    grid[charX][charY] = grid[charX][nextPos]
                    grid[charX][nextPos] = characterPos
                    charY = charY + 1
                    playerMovementSound.play(0)
        elif keys[pygame.K_w] and grid[charX - 1][charY] != "X":
            if grid[charX - 1][charY] != "D" or doorOpened == True:
                if grid[charX - 1][charY] != "E" or exit == True:
                    charIndex = 3
                    nextPos = charX-1
                    characterPos = grid[charX][charY]
                    grid[charX][charY] = grid[nextPos][charY]
                    grid[nextPos][charY] = characterPos
                    charX = charX - 1
                    playerMovementSound.play(0)
        elif keys[pygame.K_s] and grid[charX + 1][charY] != "X":
            if grid[charX + 1][charY] != "D" or doorOpened == True:
                if grid[charX + 1][charY] != "E" or exit == True:
                    charIndex = 0
                    nextPos = charX + 1
                    characterPos = grid[charX][charY]
                    grid[charX][charY] = grid[nextPos][charY]
                    grid[nextPos][charY] = characterPos
                    charX = charX + 1
                    playerMovementSound.play(0)

def handleKeysandGameState(): #handles gameStare and keys pressed, called from main
    global gameState, rectIndex, countdownTimer, numSwitchesCompleted, switch1Connected, switch2Connected, switch3Connected, powerOn, charX, charY, escapeRope
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN] and gameState == NEXT_LEVEL:
        gameState = START
    if keys[pygame.K_RETURN] and gameState == TITLE and rectIndex == 0:
        gameState = START
    if keys[pygame.K_RETURN] and gameState == GAME_OVER and rectIndex == 0:
        init()
    if keys[pygame.K_RETURN] and gameState == WIN and rectIndex == 0:
        init()
    if keys[pygame.K_RETURN] and gameState != START and gameState != QUIT and rectIndex == 1:
        gameState = QUIT
    if gameState == TITLE or gameState == GAME_OVER or gameState == WIN:#handle selector for draw
        if keys[pygame.K_UP]:
            rectIndex = 0
        if keys[pygame.K_DOWN]:
            rectIndex = 1
    if gameState == START:  # handles switches, power, powerUp and game conditions
        if charX == switch1X and charY == switch1Y and keys[pygame.K_RETURN] and dead == False and switch1Connected == False:
            numSwitchesCompleted += 1
            switchFinishedSound.play(0)
            switch1Connected = True
        if charX == switch2X and charY == switch2Y and keys[pygame.K_RETURN] and dead == False and switch2Connected == False:
            numSwitchesCompleted += 1
            switchFinishedSound.play(0)
            switch2Connected = True
        if charX == switch3X and charY == switch3Y and keys[pygame.K_RETURN] and dead == False and switch3Connected == False:
            numSwitchesCompleted += 1
            switchFinishedSound.play(0)
            switch3Connected = True
        if charX == powerX and charY == powerY and keys[pygame.K_RETURN] and switchesCompleted == True and powerOn == False:
            objectiveCompleteSound.play(0)
            powerOn = True

def main():
    global gameState, timer
    pygame.init()
    init()
    clock = pygame.time.Clock()
    while gameState != QUIT:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState = QUIT
            if event.type == pygame.KEYDOWN:
                handleKeysandGameState()
                if gameState == START:
                    playerMovement()
        update()
        draw()
    pygame.quit()

if __name__ == "__main__":
    main()