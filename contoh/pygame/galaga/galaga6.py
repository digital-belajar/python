# lanjutan dari galaga1.py
# tambahan:
#    tembakan missile

# inisialisasi
import pygame
from ship import Ship
from missile2 import Missile2
from drone import Drone
from destroyer import Destroyer
import random

pygame.init()
screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()

p1 = Ship(screen)
missile1 = Missile2(screen)
drones = [
    Drone(screen),
    Drone(screen),
    Drone(screen),
    Destroyer(screen),
    Destroyer(screen)
]

for obj in drones:
    obj.spawn(random.randint(10,450),random.randint(10,300))

img_stage = pygame.image.load('stage.png')
sound_missile = pygame.mixer.Sound('shot.wav')

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
            sound_missile.play()
            missile1.launch(p1.x+16, p1.y)

    # menggambar latar
    screen.blit(img_stage,(0,0))
    
    # gerakan missile    
    if missile1.launched:
        missile1.move()
        missile1.draw()   

    for obj in drones:
        if missile1.get_rect().colliderect(obj.get_rect()):
            obj.destroy()
            missile1.gone()
        else:
            obj.move()
        obj.draw()

    # gambar pesawat
    p1.draw()

    # update windows
    pygame.display.flip()
    clock.tick(20) 

pygame.quit()

