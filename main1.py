import sys, pygame, random, pandas as pd
from ship import Ship
from asteroid import Asteroid
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

# set the width and height to the size of the screen
size = (width, height) = (int(screen_info.current_w * 0.5), int(screen_info.current_h * 0.5))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (30, 0, 30)
screen.fill(color)

# read and store game data
df = pd.read_csv('game_info.csv')

# Setup Game Variables
Asteroids = pygame.sprite.Group()
NumLevels = df['LevelNum'].max()
Level = df['LevelNum'].min()
LevelData = df.iloc[Level]
AsteroidCount = LevelData['AsteroidCount']
Player = Ship((LevelData['PlayerX'], LevelData['PlayerY']))


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