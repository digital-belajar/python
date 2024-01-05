# lanjutan dari galaga1.py
# tambahan:
#    tembakan missile

# inisialisasi
import pygame
from ship import Ship
from missile import Missile

pygame.init()
screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()

p1 = Ship(screen)
missile1 = Missile(screen) 
img_stage = pygame.image.load('stage.png')

running = True
while running: # selama running bernilai True, ulangi proses

    # check event
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        p1.move_left()
    if keys[pygame.K_RIGHT]:
        p1.move_right()   
    if keys[pygame.K_SPACE]:
        if missile1.launched == False:
            missile1.launch(p1.x+16, p1.y)

    # menggambar latar
    screen.blit(img_stage,(0,0))
    
    
    if missile1.launched:
        missile1.move()
        missile1.draw()   

    # gambar pesawat
    p1.draw()

    # update windows
    pygame.display.flip()
    clock.tick(20) 

pygame.quit()

