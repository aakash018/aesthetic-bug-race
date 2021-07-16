import pygame
import random
from time import sleep
from math import floor

W = 800
H = 600
pygame.init()
screen = pygame.display.set_mode([W, H])
bug_black = pygame.image.load("./img/animal.png")
bug_red = pygame.image.load("./img/animal_2.png")
bug_red2 = pygame.image.load("./img/animal_3.png")
bugX = 200
bugY = 470
bugY_red = 470
bugY_red2 = 470
bugY_line = bugY + 30
bugY_change = 0
bugY_red_speed = 0
bugY_red2_speed = 0


def restart():
    global bugX, bugY, bugY_red, bugY_red2
    bugX = 200
    bugY = 470
    bugY_red = 470
    bugY_red2 = 470


def random_speed():
    return random.randint(2, 7) / 100


def change(position):
    global bugY_change, bugY_red_speed, bugY_red2_speed
    if floor(bugY) == position:
        bugY_change = random_speed()
    if floor(bugY_red) == position:
        bugY_red_speed = random_speed()
    if floor(bugY_red2) == position:
        bugY_red2_speed = random_speed()


def bug():
    global bugX, bugY, bugY_red, bugY_red2, bugY_change, bugY_red_speed, bugY_red2_speed
    if bugY < 40:
        bugY_change = 0
    if bugY_red < 40:
        bugY_red_speed = 0
    if bugY_red2 < 40:
        bugY_red2_speed = 0

    if bugY < 40 and bugY_red < 40 and bugY_red2 < 40:
        sleep(1)
        restart()

    if bugY == 470 and bugY_red2 == 470 and bugY_red == 470:
        bugY_change = random_speed()
        bugY_red_speed = random_speed()
        bugY_red2_speed = random_speed()

    change(350)
    change(200)

    bugY -= bugY_change
    bugY_red -= bugY_red_speed
    bugY_red2 -= bugY_red2_speed
    screen.blit(bug_black, (bugX, bugY))
    pygame.draw.line(screen, (0, 0, 0), (bugX + 15, bugY_line), (bugX + 15, bugY + 25))
    pygame.draw.line(screen, (255, 100, 100), (bugX + 15 + 150, bugY_line), (bugX + 15 + 150, bugY_red + 25))
    pygame.draw.line(screen, (255, 200, 200), (bugX + 15 + 150 + 150, bugY_line),
                     (bugX + 15 + 150 + 150, bugY_red2 + 30))
    screen.blit(bug_red, (bugX + 150, bugY_red))
    screen.blit(bug_red2, (bugX + 150 + 150, bugY_red2))


class Line:
    def __init__(self):
        pygame.draw.line(screen, (0, 0, 0), (180, 500), (620, 500))
        pygame.draw.line(screen, (0, 0, 0), (180, 70), (620, 70))


flag = True


def main_loop():
    global screen
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
        screen.fill((255, 255, 200))
        bug()
        line = Line()
        pygame.display.update()


main_loop()
