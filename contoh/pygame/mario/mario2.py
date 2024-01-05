# deskripsi:
#  implementasi Class mario

# inisialisasi
import pygame
from mario import Mario

pygame.init()
screen = pygame.display.set_mode([700,500])
clock = pygame.time.Clock()


mario = Mario(screen)

#mario = pygame.transform.flip(mario, True, False)
bg = pygame.image.load('img/w1-1.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False            
            if event.key == pygame.K_SPACE:
                mario.jump(8)

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario.move_left()
    elif keys[pygame.K_RIGHT]:
        mario.move_right()
    else:
        mario.stand()

    mario.gravity()
    screen.blit(bg,(0,0))
    mario.draw()
    
    pygame.display.flip()
    clock.tick(18)

pygame.quit()

