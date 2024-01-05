# inisialisasi
import pygame

pygame.init()
screen = pygame.display.set_mode([1024,568])
clock = pygame.time.Clock()

ground = 450
y = ground
x = 30
speed = 10
# https://github.com/pujangga123/files/blob/main/python/mario/img/mario.png
mario = pygame.image.load('img/mario0.png')

# https://github.com/pujangga123/files/blob/main/python/mario/img/mario-level.png
bg = pygame.image.load('img/mario-level.jpg')
jump = 0

# https://github.com/pujangga123/files/blob/main/python/mario/sound/mario-jump1.wav
s_jump = pygame.mixer.Sound('sound/mario-jump1.wav')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False            
            if event.key == pygame.K_SPACE:
                jump = 20
                s_jump.play()
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 10
    if keys[pygame.K_RIGHT]:
        x += 10

    if jump>0:
        y -= 5
        jump -= 1
    elif y<ground:
        y += 5    

    #x += speed
    screen.blit(bg,(0,0))
    screen.blit(mario,(x,y))
    
    pygame.display.flip()
    clock.tick(50)

pygame.quit()

