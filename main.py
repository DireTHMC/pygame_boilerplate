import pygame
import sys
from pygame.color import THECOLORS
import time
import random

pygame.init()

# Создание экрана
display_width = 400
display_height = 800
screen = pygame.display.set_mode((display_width, display_height))

# Название
pygame.display.set_caption("Don't crush my car, dude!")

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#Модуль для времени, чтобы мониторить кадры в секунду
clock = pygame.time.Clock()

#Создание героя
carimg = pygame.image.load("Image/car_aston.png")
carimg = pygame.transform.scale(carimg, (70, 80))
car_width = 70

#Функция для препятствий
def things(thing_x, thing_y, thing_w, thing_h, color):
    pygame.draw.rect(screen, color, [thing_x, thing_y, thing_w, thing_h])

#Отрисовка авто
def car(x, y):
    screen.blit(carimg, (x, y))

#Вывод текста
def text_objects(text , font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()

def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, largetext)
    TextRect.center = ((display_width/2), (display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(5)

    game_loop()

def crash():
    message_display('You crashed, looser!')


#Запуск игры
def game_loop():
    # Размещение авто
    x = (165)
    y = (710)

    thing_start_x = random.randrange(0, display_width)
    thing_start_y = -800
    thing_speed = 5
    thing_width = 70
    thing_height = 80

    # условия игры
    x_change = 0  # смещение
    car_speed = 0  # скорость

    gameexit = False

    while not gameexit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameexit = True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameexit = True
                    pygame.quit()

                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        #Смена позиции
        x += x_change
        #Создание фона
        screen.fill(THECOLORS["bisque3"])
        things(thing_start_x, thing_start_y, thing_width, thing_height, black)
        thing_start_y += thing_speed

        #Появление машинки
        car(x, y)
        if x > display_width - car_width or x < 0:
            gameexit = True
            crash()
        if thing_start_y > display_height:
            thing_start_y = 0 - thing_height
            thing_start_x = random.randrange(0, display_width)

        #Проверка дисплея на обновление
        pygame.display.update()
        #Кадры в секунду
        clock.tick(60)

game_loop()
pygame.quit()
quit()

