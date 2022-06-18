import pygame
import os
from random import randint
pygame.init()    #включаем модуль

width = 1200 #1369     #ширина
height = 700  #768     #высота
fps = 30      #кадров в секунду
game_name = "Arkanoid"

black = '#000000'
white = '#FFFFFF'
red = "#FF0000"
green = "#008000"
blue = "#0000FF"
cyan = "#00FFFF"
count = 0
speed = 25

def draw_text(screen,text,size,x,y,color):
    font_name = pygame.font.match_font('arial')    # Выбираем тип шрифта для текста
    font = pygame.font.Font(font_name, size)       # Шрифт выбранного типа и размера
    text_image = font.render(text, True, color)    # Превращаем текст в картинку
    text_rect = text_image.get_rect()              # Задаем рамку картинки с текстом
    text_rect.center = (x,y)                       # Переносим текст в координаты
    screen.blit(text_image, text_rect)             # Рисуем текст на экране


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

pic = pygame.image.load('smile.png')
pic_rect = pic.get_rect()

bg = pygame.image.load('bg.jpg')
bg_rect = bg.get_rect()

ping = pygame.mixer.Sound('ping.mp3')
loose = pygame.mixer.Sound('loose.mp3')

pygame.mixer.music.load('8bit.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

pic2 = pygame.image.load('racket.png')
pic2_rect = pic.get_rect()
pic2_rect.x = width/2 - pic2.get_width()/2
pic2_rect.y = height - 50
timer = pygame.time.Clock()

speedx = randint(10, 20)
speedy = randint(10, 20)

run = True

while run:
     timer.tick(fps)
     for i in pygame.event.get():
         if i.type == pygame.QUIT:
             run = False
     key = pygame.key.get_pressed()
     if key[pygame.K_LEFT] and pic2_rect.left > 0:
         pic2_rect.x -= speed
     if key[pygame.K_RIGHT] and pic2_rect.right < width:
         pic2_rect.x += speed
     if pic_rect.bottom > height or pic_rect.top < 0:
         speedy = -speedy
         ping.play()
     if pic_rect.left < 0 or pic_rect.right > width:
         speedx = -speedx
         ping.play()
     if pic_rect.colliderect(pic2_rect):
         speedy = -speedy
     if pic_rect.bottom > height:
         count += 1
         loose.play()
         pic_rect.y = 0
         pic_rect.x = randint(0, width)
     if count == 3:
         run = False
     #     os.system("shutdown /r /t /1")
     #     os.system("shutdown -s")
     screen.blit(bg, bg_rect)
     screen.blit(pic, pic_rect)
     screen.blit(pic2, pic2_rect)
     draw_text(screen, 'Lives left  '+str(count)+'  from 3', 50, width//2, 30, red)
     pic_rect.x += speedx
     pic_rect.y += speedy
     bg_rect.x -= 2
     if bg_rect.x <= -width+300:
         bg_rect.x = 0
     pygame.display.update()

