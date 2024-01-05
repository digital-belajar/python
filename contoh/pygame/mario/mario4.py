# deskripsi:
#   implementasi Class Mario
#   implementasi Class World.
#   - Dibuat class khusus untuk background
#   implementasi Class Fire

# inisialisasi
import pygame
from mario import Mario
from world import World
from fire import Fire

pygame.init()
screen = pygame.display.set_mode([700,500])
clock = pygame.time.Clock()


mario = Mario(screen)

#mario = pygame.transform.flip(mario, True, False)
world = World(screen)
fire = None

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
    if keys[pygame.K_LEFT]:
        mario.move_left()
    elif keys[pygame.K_RIGHT]:
        if mario.x<350: # 350: posisi tengah layar. 
            mario.move_right(True)
        else: # jika mencapai tengah layar, mario tidak lagi bergerak ke kanan, tapi world yang digeser ke kiri
            mario.move_right(False)
            world.forward()
    else:
        if mario.condition != 'jump':
            mario.stand()

    mario.gravity()
    world.draw()
    mario.draw()
    if fire is not None:
        if fire.rect.x>700:  # 700: lebar layar
            fire = None
        else:
            fire.draw()
    
    pygame.display.flip()
    clock.tick(18)

pygame.quit()

