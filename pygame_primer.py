import pygame
import random

#class for player declaration here
class Player(pygame.sprite.Sprite):
    def __init__(self):
        #call pygame sprite constructor
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
        #add a lives option
        self.lives = 0;

    def update(self,pressed_keys):
        #move player based on input
        if pressed_keys[pygame.K_w]:
            self.rect.move_ip(0,-5)
        if pressed_keys[pygame.K_s]:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_a]:
            self.rect.move_ip(-5,0)
        if pressed_keys[pygame.K_d]:
            self.rect.move_ip(5,0)

        #keep player on the screen so they cant go out of bounds
        #check each left right(x) bottom top (y) for out of bounds
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600

#make a class for enemies
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        #call parent constructor
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((20,10))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = (random.randint(820,900),random.randint(0,600)))
        self.x_speed = random.randint(5,20)
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()



#initialize pygame objects
pygame.init()

#create the scrre object
screen = pygame.display.set_mode((800,600))

#create an instance of our player class
player = Player()

#create add enemy event
add_enemy = pygame.USEREVENT + 1

#make the add_enemy event happen every 250 milliseconds
pygame.time.set_timer(add_enemy,250)

#variable for main loop running
running = True

#create a background to then add screnn fills to keep sprite movement showing
background = pygame.Surface(screen.get_size())
background.fill((0,0,0))

#create pygame sprites groups
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

while running:
    #first loop through the event queue
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == add_enemy:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    #blit the background each time in order to make sprite visual changes occur
    screen.blit(background,(0,0))

#get player input
    pressed_keys = pygame.key.get_pressed()
#update player rect
    player.update(pressed_keys)
#update enemy rect position
    enemies.update()

    #for all sprites update visually update their state
    for objects in all_sprites:
        screen.blit(objects.surf,objects.rect)

    if pygame.sprite.spritecollideany(player,enemies):
        player.kill()


    #update screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)


''' what changed to make this collision work,
first when screen blitting use the instance.rect() as the second
argument in order to make sure you have a general idea where the rect objects are

second use sprite groups to make changes like blits to a bunch of sprites at once

third dont USE rect.move to add movement limits for players if they try to pass it just set
rect.<side> to that value

USE PAPER TO VISUALIZE DESIGN FIRST

'''
