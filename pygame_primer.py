#developer notes
#add a lives option
#add a redo option
#add in assets
#make bombs possible for tough situations
#make different types of enemies
#make clouds show up!!!!!!!(FIRST)
import pygame
import random
import time
import sys

#class for player declaration here
class Player(pygame.sprite.Sprite):
    def __init__(self):
        #call pygame sprite constructor
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load('/home/anorak/Documents/projects/pygame_learning/pygame_assets/plane.png')
        #testing surface
        #for rectangle player object
        #self.surf = pygame.Surface((75,25))
        #self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect()

        #for future use
        self.lives = 0;

    def update(self,pressed_keys):
        #move player based on input
        if pressed_keys[pygame.K_w]:
            self.rect.move_ip(0,-6)
        if pressed_keys[pygame.K_s]:
            self.rect.move_ip(0,6)
        if pressed_keys[pygame.K_a]:
            self.rect.move_ip(-6,0)
        if pressed_keys[pygame.K_d]:
            self.rect.move_ip(6,0)

        #keep player on the screen so they cant go out of bounds
        #check each left right(x) bottom top (y) for out of bounds
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 800:
            self.rect.bottom = 800

#make a class for enemies
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        #call parent constructor
        pygame.sprite.Sprite.__init__(self)
        #self.surf = pygame.Surface((20,10))
        #self.surf.fill((255,255,255))
        self.surf = pygame.image.load('/home/anorak/Documents/projects/pygame_learning/pygame_assets/missile.png')
        self.rect = self.surf.get_rect(center = (random.randint(820,900),random.randint(0,800)))
        self.speed = random.randint(5,20)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load('/home/anorak/Documents/projects/pygame_learning/pygame_assets/cloud_2.png')
        self.rect = self.surf.get_rect(center = (random.randint(810,900),random.randint(0,800)))
        self.speed = random.randint(3,5)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()


def main():
    #initialize pygame objects
    pygame.init()

    #create the screen background object
    screen = pygame.display.set_mode((800,800))

    #create an instance of our player class
    player = Player()

    #creates add enemy event
    add_enemy = pygame.USEREVENT + 1

    #creates add cloud event
    add_cloud = pygame.USEREVENT + 2


    #make the add_enemy event happen every 200 milliseconds
    pygame.time.set_timer(add_enemy,200)


    #make the add_cloud event happen every 400 milliseconds
    pygame.time.set_timer(add_cloud,200)

    #variable for main loop running
    running = True

    #create a background to then add screnn fills to keep sprite movement showing
    background = pygame.Surface(screen.get_size())
    background.fill((135,206,235))

    #create pygame sprites groups
    enemies = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    #starts time for game
    start = time.time()
    #MAIN GAME LOOP
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
            elif event.type == add_cloud:
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)

        #blit the background each time in order to make sprite visual changes occur
        screen.blit(background,(0,0))

        #get player input
        pressed_keys = pygame.key.get_pressed()
        #update player rect
        player.update(pressed_keys)
        #update enemy group rect position
        enemies.update()

        #cloud group update rect position
        clouds.update()

        #for all sprites update visually update their state
        for objects in all_sprites:
            screen.blit(objects.surf,objects.rect)

        #update whole screen
        pygame.display.flip()
        #set speed to 60 degrees
        pygame.time.Clock().tick(60)

        #check for player and enemy collision
        if pygame.sprite.spritecollideany(player,enemies):
            player.kill()
            '''
            again = raw_input("Do you want to play again?")
            if (again == "Y" or again == "y"):
                main()
            else:
                '''
            #gets end time for game and then prints total time elapsed
            end = time.time()
            print(end-start)
            #pygame.quit()
            sys.exit(0)

        ''' what changed to make this collision work,
        first when screen blitting use the instance.rect() as the second
        argument in order to make sure you have a general idea where the rect objects are

        second use sprite groups to make changes like blits to a bunch of sprites at once

        third dont USE rect.move to add movement limits for players if they try to pass it just set
        rect.<side> to that value

        ALWAYS USE DOCUMENTATION

        KILL REMOVES SPRITE FROM ALL GROUPS

        USE SPRITE GROUPS THEY HELP A LOT

        USE PAPER TO VISUALIZE DESIGN FIRST

        '''



if __name__ == "__main__":
    main()
