import pygame, pandas as pd
from ship import Ship
'''
import sys, pygame, random, pandas as pd

from asteroid import Asteroid
from pygame.locals import *

add the following import:
from ship import Ship
Create a new instance of Ship with a tuple for the position parameter
'''



pygame.init()
screen_info = pygame.display.Info()

# set the width and height to the size of the screen
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))



screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (30, 0, 30)
screen.fill(color)



# read and store game data
df = pd.read_csv('game_info.csv')

NumLevel = df['LevelNum'].max()
CurrentLevel = df['LevelNum'].min()

LevelData = df.iloc[CurrentLevel]




#Player = Ship(())
Player = Ship((LevelData['PlayerX'], LevelData['PlayerY']))







# Setup Game Variables

NumLevels = df['LevelNum'].max()
Level = df['LevelNum'].min()
LevelData = df.iloc[Level]




def init():
    global AsteroidCount, Asteroids, LevelData
    LevelData = df.iloc[Level]
    Player.reset((LevelData['PlayerX'], LevelData['PlayerY']))
    Asteroids.empty()
    AsteroidCount = LevelData['AsteroidCount']
    for i in range(AsteroidCount):
        Asteroids.add(Asteroid((random.randint(50, width - 50), random.randint(50, height - 50)), random.randint(15, 60)))


def win():
    font = pygame.font.SysFont(None, 70)
    text = font.render("You Escaped!", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (width/2, height/2)
    while True:
        screen.fill(color)
        screen.blit(text, text_rect)
        pygame.display.flip()



'''
Define a 'main' function
global level
call "init()" function
while level is less than NumLevels

'''


def main():
    global Level
    init()
    while Level <= NumLevels:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Player.speed[0] = 10
                if event.key == pygame.K_LEFT:
                    Player.speed[0] = -10
                if event.key == pygame.K_UP:
                    Player.speed[1] = -10
                if event.key == pygame.K_DOWN:
                    Player.speed[1] = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    Player.speed[0] = 0
                if event.key == pygame.K_LEFT:
                    Player.speed[0] = 0
                if event.key == pygame.K_UP:
                    Player.speed[1] = 0
                if event.key == pygame.K_DOWN:
                    Player.speed[1] = 0

        screen.fill(color)
        Player.update()
        Asteroids.update()
        gets_hit = pygame.sprite.spritecollide(Player, Asteroids, False)
        Asteroids.draw(screen)
        screen.blit(Player.image, Player.rect)
        pygame.display.flip()

        if Player.checkReset(width):
            if Level == NumLevels:
                break
            else:
                Level += 1
                init()
        elif gets_hit:
            Player.reset((LevelData['PlayerX'], LevelData['PlayerY']))

    win()


if __name__ == '__main__':
    main()