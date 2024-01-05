# deskripsi:
#   implementasi Class mario
#   implementasi Class World.
#   - Dibuat class khusus untuk background

# inisialisasi
import pygame
from mario import Mario
from world import World

pygame.init()
screen = pygame.display.set_mode([700,500])
clock = pygame.time.Clock()


mario = Mario(screen)

world = World(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False            
            if event.key == pygame.K_SPACE:
                mario.jump(11)

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario.move_left()
    elif keys[pygame.K_RIGHT]:
        if mario.x<350:
            mario.move_right(True)
        else:
            mario.move_right(False)
            world.forward()
    else:
        if mario.condition != 'jump':
            mario.stand()

    mario.gravity()
    world.draw()
    mario.draw()
    
    pygame.display.flip()
    clock.tick(18)

pygame.quit()

