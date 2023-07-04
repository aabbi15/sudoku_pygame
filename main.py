import pygame
from pygame.locals import *
import newbutton
import sys
import random
import sudokumaker
import dragndrop
import asyncio

pygame.init()

# Set up the screen
w = 1200
h = 800
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("SUDOKU")

# Set up the fonts
titlefont = pygame.font.SysFont("Arial", 70)
myfont = pygame.font.SysFont("Times", 40)

# Set up the images
board_img = pygame.image.load("sudokuboard.jpg")
one_img = pygame.image.load("one.png").convert_alpha()
two_img = pygame.image.load("two.png").convert_alpha()
three_img = pygame.image.load("three.png").convert_alpha()
four_img = pygame.image.load("four.png").convert_alpha()
five_img = pygame.image.load("five.png").convert_alpha()
six_img = pygame.image.load("six.png").convert_alpha()
seven_img = pygame.image.load("seven.png").convert_alpha()
eight_img = pygame.image.load("eight.png").convert_alpha()
nine_img = pygame.image.load("nine.png").convert_alpha()
redbox_img = pygame.image.load("redbox.png").convert_alpha()
blank_img = pygame.image.load("blank.png").convert_alpha()
redbox_img = pygame.transform.scale(redbox_img, (75, 75))

numbers_img = [blank_img, one_img, two_img, three_img, four_img, five_img, six_img, seven_img, eight_img, nine_img]
bar_img = pygame.image.load("emptybar.jpg")

# Set up the game logic
difficulty = "hard"
finalgrid = sudokumaker.generatepuzzle(difficulty)
empty_coordinates = []
empty_rect = []
filled_rect = []
current_tries = 3
timer_value = 0
timer_started = False

for i in range(9):
    for j in range(9):
        if finalgrid[i][j] == 0:
            empty_coordinates.append(((78 * i), (j * 78)))

for x, y in empty_coordinates:
    empty_rect.append(pygame.Rect(x, y, 78, 78))

# Set up the dragger
dragger = [0] * 10
for i in range(1, 10):
    dragger[i] = dragndrop.DragnDrop(screen, numbers_img[i], (78 * (i - 1)), 722)

# Set up the buttons
menu_buttons = [
    newbutton.Button(screen, 510, 180, ["red", "blue", "green"], 200, 50, newgamepressed, "New Game"),
    newbutton.Button(screen, 510, 280, ["red", "blue", "green"], 200, 50, myfunction, "Continue"),
    newbutton.Button(screen, 510, 380, ["red", "blue", "green"], 200, 50, myfunction, "Settings"),
    newbutton.Button(screen, 510, 480, ["red", "blue", "green"], 200, 50, myfunction, "Exit")
]

level_buttons = [
    newbutton.Button(screen, 510, 180, ["red", "blue", "green"], 200, 50, easypress, "Easy"),
    newbutton.Button(screen, 510, 280, ["red", "blue", "green"], 200, 50, mediumpress, "Medium"),
    newbutton.Button(screen, 510, 380, ["red", "blue", "green"], 200, 50, hardpress, "Hard"),
    newbutton.Button(screen, 510, 480, ["red", "blue", "green"], 200, 50, expertpress, "Expert"),
    newbutton.Button(screen, 510, 580, ["red", "blue", "green"], 200, 50, backpress, "Back")
]

# Set up the game loop
running = True
currentx = -1
currenty = -1
tempgrid = [[0] * 9 for _ in range(9)]
keyentered = False


def newgamepressed():
    global finalgrid, empty_coordinates, empty_rect, current_tries, timer_value, timer_started
    finalgrid = sudokumaker.generatepuzzle(difficulty)
    empty_coordinates = []
    empty_rect = []
    filled_rect = []
    current_tries = 3
    timer_value = 0
    timer_started = False

    for i in range(9):
        for j in range(9):
            if finalgrid[i][j] == 0:
                empty_coordinates.append(((78 * i), (j * 78)))

    for x, y in empty_coordinates:
        empty_rect.append(pygame.Rect(x, y, 78, 78))

    for button in menu_buttons:
        button.deactivate()


def myfunction():
    print("This button does nothing.")


def easypress():
    global difficulty
    difficulty = "easy"


def mediumpress():
    global difficulty
    difficulty = "medium"


def hardpress():
    global difficulty
    difficulty = "hard"


def expertpress():
    global difficulty
    difficulty = "expert"


def backpress():
    pass


def checkwin():
    global finalgrid
    for i in range(9):
        for j in range(9):
            if finalgrid[i][j] == 0 or finalgrid[i][j] != tempgrid[i][j]:
                return False
    return True


def drawredbox(x, y):
    screen.blit(redbox_img, (x, y))


def redraw_screen():
    screen.fill((255, 255, 255))
    screen.blit(board_img, (0, 0))
    screen.blit(bar_img, (0, 700))

    if currentx != -1 and currenty != -1:
        drawredbox(currentx, currenty)

    timer_text = myfont.render("Time: " + str(timer_value), 1, (0, 0, 0))
    screen.blit(timer_text, (920, 730))

    tries_text = myfont.render("Tries: " + str(current_tries), 1, (0, 0, 0))
    screen.blit(tries_text, (600, 730))

    for i in range(1, 10):
        dragger[i].draw()

    for rect in empty_rect:
        pygame.draw.rect(screen, (255, 255, 255), rect)

    for i in range(9):
        for j in range(9):
            if tempgrid[i][j] != 0:
                screen.blit(numbers_img[tempgrid[i][j]], (78 * i, 78 * j))

    if checkwin():
        win_text = titlefont.render("YOU WIN!", 1, (0, 0, 0))
        screen.blit(win_text, (400, 350))

    pygame.display.update()


def decrement_tries():
    global current_tries
    current_tries -= 1
    if current_tries == 0:
        game_over()


def game_over():
    print("Game Over")


# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()

                for button in menu_buttons:
                    if button.rect.collidepoint(pos):
                        button.call_function()

                for button in level_buttons:
                    if button.rect.collidepoint(pos):
                        button.call_function()

                for rect in empty_rect:
                    if rect.collidepoint(pos) and current_tries > 0:
                        currentx, currenty = rect.x, rect.y

                for i in range(1, 10):
                    if dragger[i].rect.collidepoint(pos) and currentx != -1 and currenty != -1:
                        tempgrid[currentx // 78][currenty // 78] = i
                        currentx, currenty = -1, -1

        if event.type == KEYDOWN:
            if event.key == K_RETURN and current_tries > 0:
                if finalgrid[currentx // 78][currenty // 78] != tempgrid[currentx // 78][currenty // 78]:
                    decrement_tries()
                else:
                    tempgrid[currentx // 78][currenty // 78] = 0
                    currentx, currenty = -1, -1

            if event.key == K_DELETE and current_tries > 0:
                tempgrid[currentx // 78][currenty // 78] = 0
                currentx, currenty = -1, -1

            if event.key == K_ESCAPE:
                currentx, currenty = -1, -1

            if event.key == K_SPACE and not timer_started:
                timer_started = True
                loop = asyncio.get_event_loop()
                loop.create_task(update_timer())

            if event.key == K_BACKSPACE:
                for button in menu_buttons:
                    button.activate()

                for button in level_buttons:
                    button.deactivate()

            if currentx != -1 and currenty != -1:
                if event.key == K_1:
                    tempgrid[currentx // 78][currenty // 78] = 1
                    currentx, currenty = -1, -1

                if event.key == K_2:
                    tempgrid[currentx // 78][currenty // 78] = 2
                    currentx, currenty = -1, -1

                if event.key == K_3:
                    tempgrid[currentx // 78][currenty // 78] = 3
                    currentx, currenty = -1, -1

                if event.key == K_4:
                    tempgrid[currentx // 78][currenty // 78] = 4
                    currentx, currenty = -1, -1

                if event.key == K_5:
                    tempgrid[currentx // 78][currenty // 78] = 5
                    currentx, currenty = -1, -1

                if event.key == K_6:
                    tempgrid[currentx // 78][currenty // 78] = 6
                    currentx, currenty = -1, -1

                if event.key == K_7:
                    tempgrid[currentx // 78][currenty // 78] = 7
                    currentx, currenty = -1, -1

                if event.key == K_8:
                    tempgrid[currentx // 78][currenty // 78] = 8
                    currentx, currenty = -1, -1

                if event.key == K_9:
                    tempgrid[currentx // 78][currenty // 78] = 9
                    currentx, currenty = -1, -1

    redraw_screen()
