import pygame
import sys
from pygame.color import THECOLORS

pygame.init()

# Создание экрана
display_width = 1200
display_height = 800
screen = pygame.display.set_mode((display_width, display_height))

# Название
pygame.display.set_caption("Don't crush my car, dude!")

#colors
black = (0, 0, 0)
white = (255, 255, 255)

#Модуль для времени, чтобы мониторить кадры в секунду
clock = pygame.time.Clock()

#Создание героя
carimg = pygame.image.load("Image/car_aston.png")
carimg = pygame.transform.scale(carimg, (70, 80))

#Отрисовка авто
def car(x, y):
    screen.blit(carimg, (x, y))

#Запуск игры
def game_loop():
    # Размещение авто
    x = (565)
    y = (710)

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
        #Появление машинки
        car(x, y)
        #Проверка дисплея на обновление
        pygame.display.update()
        #Кадры в секунду
        clock.tick(60)

game_loop()
pygame.quit()
quit()