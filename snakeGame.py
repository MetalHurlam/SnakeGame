# Snake Game!
# by Tj

# our game imports
import pygame
import sys
import random
import time

# check for initializing errors
check_errors = pygame.init()

if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting....".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")


# Play surface

playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake game!')

# Colors
red = pygame.Color(255, 0, 0)  # Game over
green = pygame.Color(0, 255, 0)  # Snake
black = pygame.Color(0, 0, 0)  # Score
white = pygame.Color(255, 255, 255)  # background
brown = pygame.color(165, 42, 42)  # food

# FPS controller Frames per second

fpsController = pygame.time.Clock()

# Important variables
# Snake Position
SnakePos = [100, 50]
# Snake Body
snakeBody = [[100, 50], [90, 50], [80, 50]]
