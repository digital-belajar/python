# inisialisasi
import pygame
pygame.init()
screen = pygame.display.set_mode([600,500])
clock = pygame.time.Clock()
 
running = True
warna_bg = (255,255,255)
warna_bola = (0,0,255)

x = 13
speedx = 5

while running: # selama running bernilai True, ulangi proses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill( warna_bg )   

    x = x + speedx   

    pygame.draw.circle(screen,warna_bola, (x,10),10)

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
