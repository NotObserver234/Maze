from pygame import *
window = display.set_mode((700,500))
display.set_caption('Maze')
bg= transform.scale(image.load("background.jpg"),(700,500))



mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.3)
mixer.music.play(-1)





class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,width,height):
        super().__init__()
        self.image = Surface((width,height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed

class Enemy(GameSprite):
   
    direction = "left"
    def update_hor(self):
        
        if self.rect.x <= 470:
            self.direction = 'right'

        if self.rect.x >= 700 - 85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed

        else:
            self.rect.x += self.speed
    direction_2 = 'up'
    def update_ver(self):
        if self.rect.y == 5:
            self.direction_2 = 'down'

        if self.rect.y == 80:
            self.direction_2 = 'up'

        if self.direction_2 == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
   
w1 = Wall(0,255,0,150,150,10,500)
w2 = Wall(0,255,0,300,0,10,350)
w3 = Wall(0,255,0,465,100,10,500)
w4 = Wall(0,255,0,600,150,100,10)
w5 = Wall(0,255,0,470,250,100,10)
w6 = Wall(0,255,0,150,150,70,10)
w7 = Wall(0,255,0,250,250,60,10)
w8 = Wall(0,255,0,310,250,60,10)
w9 = Wall(0,255,0,300,440,10,60)
w10 = Wall(0,255,0,405,150,60,10)
hero = Player("hero.png", 50,300,5)
enemy = Enemy("cyborg.png", 500,300,4)
enemy1 = Enemy('cyborg.png', 500,45,1)
treasure = GameSprite("treasure.png",580,400,0)
game = True
finish = False

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.SysFont('Arial',70)
win = font.render('YOU WIN',True,(0,255,0))
fail = font.render('YOU LOSE',True,(255,0,0))
walls = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10]
enemies = [enemy,enemy1]

while game:
    if not finish:
        window.blit(bg,(0,0))
        hero.reset()
        enemy.reset()
        enemy1.reset()
        treasure.reset()
        hero.update()
        enemy.update_hor()
        enemy1.update_ver()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()

    for e in event.get():
        if e.type == QUIT:
            game = False


        if sprite.collide_rect(hero,treasure):
            finish = True
            money.play()
            window.blit(win,(200,200))

        for i in enemies:
            if sprite.collide_rect(hero,i):
                finish = True
                kick.play()
                window.blit(fail,(200,200))
        for i in walls:
            if sprite.collide_rect(hero,i):
                finish = True
                kick.play()
                window.blit(fail,(200,200))

   

    time.delay(10)
    display.update()