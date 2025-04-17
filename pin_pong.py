import pygame
from pygame import *
from time import *
from random import *
mixer.init()
pygame.init()
font.init()
font = font.SysFont('Arial', 40)

clock = pygame.time.Clock()
FPS = 60


window = display.set_mode((1000, 500))
display.set_caption('PIN_PONG')


background = transform.scale(image.load('Backgroung.png'), (700, 500))




win_width = 1000
win_height = 500
player_speed = 10




class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))





class Player(GameSprite):


    def update_hero(self):
        keys_press = key.get_pressed()


        if keys_press[K_w] and self.rect.x > 5:
            self.rect.x -= player_speed


        if keys_press[K_s] and self.rect.x < win_width:
            self.rect.x += player_speed


class Player2(GameSprite):
    def update_hero2(self):
        keys_press = key.get_pressed()

        if keys_press[K_UP] and self.rect.x > 5:
            self.rect.y -= player_speed


        if keys_press[K_DOWN] and self.rect.x < win_width:
            self.rect.y += player_speed




speed_x = 3
speed_y = 3


a = 0
real_time = False
num_fire = 0
PAKETKA = Player("", 50, 300, 100, 170, player_speed)
PAKETKA2 = Player2('', 850, 300, 100, 170, player_speed)
ball = GameSprite('', 400, 400, 20, 30, 6)


not_win = font.render('ЛОХ', True, (100, 50, 0))
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    



    if not finish:
        window.blit(background, (0, 0))
        PAKETKA.update()
        PAKETKA2.update()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(PAKETKA, ball) or sprite.collide_rect(PAKETKA2, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(not_win, (200, 200))



        
       
        """konec = sprite.spritecollide(PAKETA, monsters, False)
        if konec or lost >= 10:
            finish = True
            lox = font.render('ЛОХ', True, (100, 50, 0))
            window.blit(lox, (200, 200))



        text_lose = font.render('Пропущено: ' + str(lost), True, (255, 255, 255))
        text_lose2 = font.render('Сбито: ' + str(a), True, (255, 255, 255))
        window.blit(text_lose, (10, 10))
        window.blit(text_lose2, (10, 40))"""



        clock.tick(FPS)

            




        display.update()
   
    


pygame.quit()



