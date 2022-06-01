import pygame
import sys
from pygame.color import THECOLORS

pygame.init()
screen = pygame.display.set_mode((1200, 800)) #Создание экрана
screen.fill(THECOLORS["bisque3"])
pygame.display.set_caption("MyFirstGame") #Название
bg = pygame.image.load("Image/bg.img.jpg") #Создание фона
bg = pygame.transform.scale(bg, (1200, 800))
screen.blit(bg, (0, 0))

image = pygame.image.load("Image/01.png") #Создание героя
image = pygame.transform.scale(image, (50, 50))
x = 5
y = 10

screen.blit(image, (x, y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()