# deskripsi:
#   implementasi Class Mario
#   implementasi Class World.
#   - Dibuat class khusus untuk background
#   - background tidak berubah
#   implementasi Class Fire
#   implementasi Class Enemy
#   implementasi mario.die

# inisialisasi
import pygame
from mario import Mario
from world import World
from fire import Fire
from enemy import Enemy

pygame.init()
screen = pygame.display.set_mode([700,500])
clock = pygame.time.Clock()

mario = Mario(screen)
world = World(screen)
fire = None
gomba = Enemy(screen, 650,400)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False            
            if event.key == pygame.K_SPACE:
                mario.jump(11)
            if event.key == pygame.K_x:
                fire = Fire(screen,mario)
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if mario.condition!='die':
        if keys[pygame.K_LEFT]:
            mario.move_left()
        elif keys[pygame.K_RIGHT]:
            mario.move_right(True)
        else:
            if mario.condition != 'jump':
                mario.stand()

    mario.gravity()
    world.draw()
    mario.draw()

    if gomba is not None:  # jika gomba ada di layar, gerakan gomba
        gomba.move()
        gomba.draw()
        mariorect = pygame.Rect(mario.x, mario.y, 32, 32) # 32 x 32 adalah ukuran gambar mario
        if gomba.hit(mariorect):
            mario.die()

    if fire is not None: # jika ada api dilayar ...
        if gomba is not None and fire.hit(gomba.rect): # check apakah ada gomba dan api mengenai gomba
            #gomba = None                    # hapus gomba
            fire.hit_enemy()
            gomba = Enemy(screen, 650,400)   # reset gomba
            fire = None                      # hapus api
        else:
            if fire.rect.x>700 or fire.rect.x<0: # 700: lebar layar
                fire = None  # jika api melewati layar, hapus api
            else:
                fire.draw()
    
    pygame.display.flip()
    clock.tick(18)

pygame.quit()