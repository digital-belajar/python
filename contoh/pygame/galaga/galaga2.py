# contoh program seperti pg9.py 
# tambahan:
#    radius, color, xspeed, yspeed menjadi properti bola
#    fungsi move ditambahkan untuk melakukan pergerakan

# inisialisasi
import pygame
from ship_turbo import ShipTurbo

pygame.init()
screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()

p1 = ShipTurbo(screen)

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
    if keys[pygame.K_UP]:
        p1.move_up()
    if keys[pygame.K_DOWN]:
        p1.move_down() 

    # isi screen dengan kode warna RGB 255,255,255 (warna putih)
    screen.fill((0,0,0))    
    
    p1.draw()

    # update windows
    pygame.display.flip()
    clock.tick(20) 

pygame.quit()

