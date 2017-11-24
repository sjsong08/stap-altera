# Simulate (a Simon clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import random, sys, time, pygame
from pygame.locals import *
import time
import serial
import numpy as np
from sklearn import svm

def normalization (input):
    s = input.shape[0]
    for i in range (s):
        input[i,:] = input[i,:]/np.max(input[i,:])
    return input

test = serial.Serial(port="COM3",baudrate=921600)
DS1 = np.loadtxt('data/1122.txt', unpack=True, dtype='float32').reshape([64,35])
DS2 = np.loadtxt('data/1124.txt', unpack=True, dtype='float32').reshape([64,35])
DS3 = np.loadtxt('data/11242.txt', unpack=True, dtype='float32').reshape([64,35])
DS4 = np.loadtxt('data/11243.txt', unpack=True, dtype='float32').reshape([64,35])
DS = np.concatenate([DS1,DS3,DS4],1)
DS = DS.transpose()
DS = normalization(DS)

Label = np.repeat(np.array([1,2,3,4,5,6,7]), 5)
Label = np.resize(Label, 35*3)

CLF = svm.SVC()
CLF.fit(DS,Label)

input = 1



FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FLASHSPEED = 500  # in milliseconds
FLASHDELAY = 200  # in milliseconds
TIMEOUT = 4  # seconds before game over if no button is pushed.
DARKGRAY = (40, 40, 40)
BLACK = (0, 0, 0)

b1 = (40, 160)
b2 = (60, 270)
b3 = (180, 320)
b4 = (290, 320)
b5 = (400, 320)
b6 = (520, 270)
b7 = (540, 160)

"""
# Rect objects for each of the four buttons
YELLOWRECT = pygame.Rect(40, 160, BUTTONSIZE, BUTTONSIZE)
PINKRECT   = pygame.Rect(60, 270, BUTTONSIZE, BUTTONSIZE)
BLUERECT   = pygame.Rect(180, 320, BUTTONSIZE, BUTTONSIZE)
GRAYRECT   = pygame.Rect(290, 320, BUTTONSIZE, BUTTONSIZE)
REDRECT    = pygame.Rect(400, 320, BUTTONSIZE, BUTTONSIZE)
SKYRECT    = pygame.Rect(520, 270, BUTTONSIZE, BUTTONSIZE)
GREENRECT  = pygame.Rect(540, 160, BUTTONSIZE, BUTTONSIZE)
"""


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, on, off1, off2, off3, off4, off5, off6, off7

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
    pattern = []  # stores the pattern of colors
    currentStep = 0  # the color the player must push next
    lastClickTime = 0  # timestamp of the player's last button push
    score = 0
    # when False, the pattern is playing. when True, waiting for the player to click a colored button:
    start = False
    waitingForInput = True

    while True:

        input = raw_input(">> ")

        test.write(input + '\r\n')
        out = ' '
        time.sleep(1)
        # OUT = []
        while True:
            OUT = []
            out = ''
            while test.inWaiting() > 0:
                out += test.read()

            if out != '':
                OUT.append(out)

            if len(OUT) > 0:
                sOut = OUT[0].split('\n')
                print ('length of sOut : ', len(sOut))

                inSample = np.zeros([1, len(sOut) - 1])
                if len(sOut) == 65:
                    for j in range(len(sOut) - 1):
                        inSample[0, j] = int(sOut[j])
                    print inSample
                    inSample = normalization(inSample)
                    finalOut = CLF.predict([inSample[0, :]])
                    print finalOut[0]
    
            clickedButton = None  # button that was clicked (set to YELLOW, RED, GREEN, or BLUE)
            DISPLAYSURF.fill([255, 255, 255])
            drawButtons()
            scoreSurf = BASICFONT.render('Score: ' + str(score), 1, BLACK)
            scoreRect = scoreSurf.get_rect()
            scoreRect.topleft = (WINDOWWIDTH - 100, 10)

            DISPLAYSURF.blit(scoreSurf, scoreRect)
            DISPLAYSURF.blit(phone_image, [140, 100])
            DISPLAYSURF.blit(infoSurf, infoRect)

            checkForQuit()

            clickedButton = user_input()

            if pygame.key.get_pressed()[pygame.K_q]:
                start = True
                waitingForInput = False

            if not waitingForInput:
                # play the pattern
                pygame.display.update()
                pygame.time.wait(1000)
                pattern.append(random.choice((b1, b2, b3, b4, b5, b6, b7)))
                for button in pattern:
                    flashButtonAnimation(button)
                    # drawButtons()
                    pygame.time.wait(FLASHDELAY)
                waitingForInput = True
            elif start == True and waitingForInput == True:
                # wait for the player to enter buttons
                if clickedButton and clickedButton == pattern[currentStep]:
                    # pushed the correct button
                    flashButtonAnimation(clickedButton)
                    currentStep += 1
                    lastClickTime = time.time()

                    if currentStep == len(pattern):
                        # pushed the last button in the pattern
                        # changeBackgroundAnimation()
                        score += 1
                        waitingForInput = False
                        currentStep = 0  # reset back to first step

                elif (clickedButton and clickedButton != pattern[currentStep]) or (
                        currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
                    # pushed the incorrect button, or has timed out
                    gameOverAnimation()
                    # reset the variables for a new game:
                    pattern = []
                    currentStep = 0
                    waitingForInput = False
                    score = 0
                    pygame.time.wait(1000)
                    # changeBackgroundAnimation()

            pygame.display.update()
            FPSCLOCK.tick(FPS)


def user_input():
    clickedButton1 = ''
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
    DISPLAYSURF.blit(off1, b1)
    DISPLAYSURF.blit(off2, b2)
    DISPLAYSURF.blit(off3, b3)
    DISPLAYSURF.blit(off4, b4)
    DISPLAYSURF.blit(off5, b5)
    DISPLAYSURF.blit(off6, b6)
    DISPLAYSURF.blit(off7, b7)


def terminate():
    pygame.quit()
    # top.mainloop()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        terminate()  # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate()  # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event)  # put the other KEYUP event objects back


def flashButtonAnimation(button_n, animationSpeed=50):
    global off1, off2, off3, off4, off5, off6, off7

    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface((60, 60))
    flashSurf = flashSurf.convert_alpha()

    for start, end, step in ((0, 255, 1), (255, 0, -1)):  # animation loop
        for alpha in range(start, end, animationSpeed * step):
            checkForQuit()
            DISPLAYSURF.blit(origSurf, (0, 0))
            DISPLAYSURF.blit(on, button_n)
            pygame.display.update()
            FPSCLOCK.tick(FPS)
    DISPLAYSURF.blit(origSurf, (0, 0))
    pygame.display.update()


def gameOverAnimation(color=DARKGRAY, animationSpeed=50):
    # play all beeps at once, then flash the background
    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface(DISPLAYSURF.get_size())
    flashSurf = flashSurf.convert_alpha()

    r, g, b = color
    for i in range(3):  # do the flash 3 times
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            # The first iteration in this loop sets the following for loop
            # to go from 0 to 255, the second from 255 to 0.
            for alpha in range(start, end, animationSpeed * step):  # animation loop
                # alpha means transparency. 255 is opaque, 0 is invisible
                checkForQuit()
                flashSurf.fill((r, g, b, alpha))
                DISPLAYSURF.blit(origSurf, (0, 0))
                DISPLAYSURF.blit(flashSurf, (0, 0))

                pygame.display.update()
                FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
