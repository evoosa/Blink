import requests
import pygame
from time import sleep
import os

# CONSTS
IMG_DIR = r"C:\Users\evoosa\Desktop\Projects\Python\BlinkRandom"
RESOLUTION = (1920, 1080)
SCREEN_SIZE = (1536, 864)
IMG_URL = "https://loremflickr.com/{w}/{h}".format(w=RESOLUTION[0], h=RESOLUTION[1])
IMG_FILENAME = 'BlinkImage.jpeg'
IMG_PATH = os.path.join(IMG_DIR, IMG_FILENAME)

# Blink the image
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, pygame.NOFRAME)
img = pygame.image.load(IMG_PATH).convert_alpha()
rect = img.get_rect()
img_center_location = [(SCREEN_SIZE[0] - rect.width) / 2, (SCREEN_SIZE[1] - rect.height) / 2]
screen.blit(img, img_center_location)
pygame.display.flip()
sleep(0.8)

quit()
