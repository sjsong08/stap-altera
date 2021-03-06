# Simulate (a Simon clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import random, sys, time, pygame
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FLASHSPEED = 500 # in milliseconds
FLASHDELAY = 200 # in milliseconds
TIMEOUT = 4 # seconds before game over if no button is pushed.

# Rect objects for each of the four buttons
YELLOWRECT = pygame.Rect(40, 160, BUTTONSIZE, BUTTONSIZE)
PINKRECT   = pygame.Rect(60, 270, BUTTONSIZE, BUTTONSIZE)
BLUERECT   = pygame.Rect(180, 320, BUTTONSIZE, BUTTONSIZE)
GRAYRECT   = pygame.Rect(290, 320, BUTTONSIZE, BUTTONSIZE)
REDRECT    = pygame.Rect(400, 320, BUTTONSIZE, BUTTONSIZE)
SKYRECT    = pygame.Rect(520, 270, BUTTONSIZE, BUTTONSIZE)
GREENRECT  = pygame.Rect(540, 160, BUTTONSIZE, BUTTONSIZE)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    phone_image = pygame.image.load("phone_image.png")
    on = pygame.image.load("on.png")
    off1 = pygame.image.load("off1.png")
    off2 = pygame.image.load("off2.png")
    off3 = pygame.image.load("off3.png")
    off4 = pygame.image.load("off4.png")
    off5 = pygame.image.load("off5.png")
    off6 = pygame.image.load("off6.png")
    off7 = pygame.image.load("off7.png")
    pygame.display.set_caption('Simulate')

    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
    infoSurf = BASICFONT.render('Press Q, Match the pattern by TAPPING 7 districts.', 1, DARKGRAY)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (10, WINDOWHEIGHT - 25)


    # Initialize some variables for a new game
    pattern = [] # stores the pattern of colors
    currentStep = 0 # the color the player must push next
    lastClickTime = 0 # timestamp of the player's last button push
    score = 0
    # when False, the pattern is playing. when True, waiting for the player to click a colored button:
    waitingForInput = True

    while True: # main game loop
        clickedButton = None # button that was clicked (set to YELLOW, RED, GREEN, or BLUE)
        DISPLAYSURF.fill([255,255,255])
        drawButtons()
        scoreSurf = BASICFONT.render('Score: ' + str(score), 1, BLACK)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 100, 10)
        
        DISPLAYSURF.blit(scoreSurf, scoreRect)
        DISPLAYSURF.blit(phone_image, [140,100])
        DISPLAYSURF.blit(infoSurf, infoRect)

        checkForQuit()
        
        clickedButton = user_input()
            

        if pygame.key.get_pressed()[pygame.K_q]:
            waitingForInput = False

        if not waitingForInput:
            # play the pattern
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice((b1,b2,b3,b4,b5,b6,b7)))
            for button in pattern:
                flashButtonAnimation(button)
                pygame.time.wait(FLASHDELAY)
            waitingForInput = True
        else:
            # wait for the player to enter buttons
            if clickedButton and clickedButton == pattern[currentStep]:
                # pushed the correct button
                flashButtonAnimation(clickedButton)
                currentStep += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    # pushed the last button in the pattern
                    #changeBackgroundAnimation()
                    score += 1
                    waitingForInput = False
                    currentStep = 0 # reset back to first step

            elif (clickedButton and clickedButton != pattern[currentStep]) or (currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
                # pushed the incorrect button, or has timed out
                gameOverAnimation()
                # reset the variables for a new game:
                pattern = []
                currentStep = 0
                waitingForInput = False
                score = 0
                pygame.time.wait(1000)
                #changeBackgroundAnimation()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def user_input():
    clickedButton1=''
    if pygame.key.get_pressed()[pygame.K_s]:
        clickedButton1 = b1
    elif pygame.key.get_pressed()[pygame.K_d]:
        clickedButton1 = b2
    elif pygame.key.get_pressed()[pygame.K_f]:
        clickedButton1 = b3
    elif pygame.key.get_pressed()[pygame.K_SPACE]:
        clickedButton1 = b4
    elif pygame.key.get_pressed()[pygame.K_j]:
        clickedButton1 = b5
    elif pygame.key.get_pressed()[pygame.K_k]:
        clickedButton1 = b6
    elif pygame.key.get_pressed()[pygame.K_l]:
        clickedButton1 = b7
    return clickedButton1

def drawButtons():
    DISPLAYSURF.blit(off1, [40,160])
    DISPLAYSURF.blit(off2, [60,270])
    DISPLAYSURF.blit(off3, [180,320])
    DISPLAYSURF.blit(off4, [290,320])
    DISPLAYSURF.blit(off5, [400,320])
    DISPLAYSURF.blit(off6, [520,270])
    DISPLAYSURF.blit(off7, [540,160])
        

def terminate():
    pygame.quit()
    #top.mainloop()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


def flashButtonAnimation(button_n, animationSpeed=50):
    if button_n == b1:
        flashColor = TRUE
        rectangle = YELLOWRECT
    elif button_n == b2:
        flashColor = BRIGHTYELLOW
        rectangle = PINKRECT
    elif button_n == b3:
        flashColor = BRIGHTYELLOW
        rectangle = BLUERECT
    elif button_n == b4:
        flashColor = BRIGHTYELLOW
        rectangle = GRAYRECT
    elif button_n == b5:
        flashColor = BRIGHTYELLOW
        rectangle = REDRECT
    elif button_n == b6:
        flashColor = BRIGHTYELLOW
        rectangle = SKYRECT
    elif button_n == b7:
        flashColor = BRIGHTYELLOW
        rectangle = GREENRECT

    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface((60,60))
    flashSurf = flashSurf.convert_alpha()
    r, g, b = flashColor
    for start, end, step in ((0, 255, 1), (255, 0, -1)): # animation loop
        for alpha in range(start, end, animationSpeed * step):
            checkForQuit()
            DISPLAYSURF.blit(origSurf, (0, 0))
            DISPLAYSURF.blit(on, rectangle.topleft)
            pygame.display.update()
            FPSCLOCK.tick(FPS)
    DISPLAYSURF.blit(origSurf, (0, 0))


def gameOverAnimation(color=(0,0,0), animationSpeed=50):
    # play all beeps at once, then flash the background
    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface(DISPLAYSURF.get_size())
    flashSurf = flashSurf.convert_alpha()

    r, g, b = color
    for i in range(3): # do the flash 3 times
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            # The first iteration in this loop sets the following for loop
            # to go from 0 to 255, the second from 255 to 0.
            for alpha in range(start, end, animationSpeed * step): # animation loop
                # alpha means transparency. 255 is opaque, 0 is invisible
                checkForQuit()
                flashSurf.fill((r, g, b, alpha))
                DISPLAYSURF.blit(origSurf, (0, 0))
                DISPLAYSURF.blit(flashSurf, (0, 0))
                drawButtons()
                pygame.display.update()
                FPSCLOCK.tick(FPS)


if __name__ == '__main__':

    main()
