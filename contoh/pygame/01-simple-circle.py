# inisialisasi
import pygame
pygame.init()
screen = pygame.display.set_mode([600,500])

running = True
warna_bg = (255,255,255)
warna_bola = (0,0,255)

posisi_bola = (30,60)
radius_bola = 10

speedx = 5
while running: # selama running bernilai True, ulangi proses
    # event handler    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill( warna_bg )
    pygame.draw.circle(screen,warna_bola, posisi_bola,radius_bola)

    pygame.display.flip()

pygame.quit()
