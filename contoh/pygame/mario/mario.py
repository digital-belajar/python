import pygame

class Mario:
    x = 10
    y = 380    
    speed = 10
    jump_height = 0
    ground = 400
    img_walk = []
    img_walk_index = 0
    img_stand = None
    img_jump = None
    img_die = None
    sound_jump = None
    sound_die = None
    screen = None   
    direct = 'right'  # left / right
    condition = 'stand' # stand/walk/jump

    def __init__(self,screen):
        self.img_stand = pygame.image.load('img/mario0.png')
        self.img_walk = [pygame.image.load('img/mario1.png'),
                         pygame.image.load('img/mario2.png'),
                         pygame.image.load('img/mario3.png'),
        ]
        self.img_jump = pygame.image.load('img/mario4.png')
        self.img_die = pygame.image.load('img/mario6.png')
        self.sound_jump = pygame.mixer.Sound('sound/mario-jump1.wav')
        self.sound_die = pygame.mixer.Sound('sound/mario-die.wav')
        self.screen = screen

    def draw(self): # gambar mario
        img = None
        if self.condition == 'stand':
            img = self.img_stand
        if self.condition == "walk":            
            img = self.img_walk[self.img_walk_index]
            self.img_walk_index = self.img_walk_index+1 if self.img_walk_index<2 else 0            
        if self.condition == 'jump':
            img = self.img_jump
        if self.condition == 'die':
            img = self.img_die
        if self.direct == 'left': #kalau mario sedang menghadap ke kiri, FLIP gambar
            img = pygame.transform.flip(img,True,False)
        
        self.screen.blit(img,(self.x,self.y))

    def move_left(self):  # gerakan ke kiri
        self.x -= self.speed
        self.direct = 'left'
        if self.condition != 'jump':
            self.condition = 'walk'
    
    def move_right(self, move_char = True):  # bergerak ke kanan 
        if move_char: # bergerak ke kanan tapi hanya jika move_char False
            self.x += self.speed
        self.direct = 'right'
        if self.condition != 'jump':
            self.condition = 'walk'

    def stand(self):
        self.condition = 'stand'
    
    def die(self):
        if self.condition!= 'die':
            self.condition = 'die'
            self.sound_die.play()

    def gravity(self):  # gerakan jatuh
        if self.jump_height>0:
            self.y -= 15
            self.jump_height -= 1
        elif self.y<self.ground:
            self.y += 15
        else:
            self.y=self.ground
            if self.condition ==  "jump":
                self.condition = 'stand'        

    def jump(self,height): # lompat
        if self.condition!='jump':
            self.condition = 'jump'
            self.jump_height = height
            self.sound_jump.play()


