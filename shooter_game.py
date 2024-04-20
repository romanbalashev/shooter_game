#Создай собственный Шутер!

from pygame import *
from random import randint
from time import time as tm

number = 0
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()


        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
       
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
font.init()
font = font.Font(None, 23)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("shooter")
background = transform.scale(image.load("galaxy.jpg"), (700,500))
bullets = sprite.Group()
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed 
        if self.rect.y < 0:
             self.kill()
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width- 80:
            self.rect.x += self.speed

    def fire(self):

        if len(bullets) < 6:
            print(len(bullets))

            bullet = Bullet("bullet.png", self.rect.x, self.rect.y, 4 )
        
            bullets.add(bullet)

        
      


class Enemies(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 475:
            self.rect.y = 50-580
            self.rect.x = randint(80,(win_width)-80)


player = Player("rocket.png", win_width - 380 ,win_height - 80 , 7)
monsters = sprite.Group()
for i in range(6):
    enemy =  Enemies("ufo.png",randint(50,(win_width)-80), randint(0,(win_height)- 480), randint(1,3))  
    monsters.add(enemy)
score = 0
game = True
FPS = 60
while game: 
    window.blit(background,(0, 0) )
    
    for e in event.get():
        if e.type == QUIT:
            game = False 
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
                lastTime = tm()
                print(lastTime)

   
    lose = font.render("You lose!", True, (200, 245, 0))
    player.update()
 
    player.reset()
    monsters.draw(window)
    monsters.update()
    bullets.update()
    bullets.draw(window)
    
    
    sprites_list = sprite.groupcollide(monsters, bullets,True, True )
    number = len(sprites_list)
    for i in sprites_list:
        enemy =  Enemies("ufo.png",randint(50,(win_width)-80), randint(0,(win_height)- 480), randint(1,2))  
        monsters.add(enemy)
        score += 1

    sprite_list = sprite.spritecollide(player, monsters, False )
    
    
    kol = font.render("Score:", True,(255, 210, 0))    
    #kol = font.render("Score:", True, (255,210,0))
    window.blit(font.render(str(score), True, (255,210,0)),(600, 65))
    window.blit(kol, (540, 65))
    

       # window.blit(lose, (200,200))

    
        
    monsters.draw(window)
    monsters.update()
    display.update()
    clock.tick(FPS)
