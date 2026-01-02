# Persiapan File dan Aset-aset
from pygame import*
from random import choice
LEBAR = 700
TINGGI = 500
window = display.set_mode((LEBAR, TINGGI))
display.set_caption("Nama Game Kalian")

bg = transform.scale(image.load('background.png'), (LEBAR, TINGGI))
gravitasi = 0.9

class GameSprite(sprite.Sprite):
  def __init__(self, img, x, y, w, h):
      super().__init__()
      self.image = transform.scale(image.load(img), (w, h))  
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y

  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, img, x, y, w, h):
        super().__init__(img, x, y, w, h)
        self.vel_y = 0
        self.on_ground = False
        self.jump_power = 15
    
    def update(self):
        keys = key.get_pressed()
        if keys[K_SPACE] and self.on_ground:
            self.vel_y = -self.jump_power
            self.on_ground = False
        self.vel_y += gravitasi
        self.rect.y += self.vel_y
    
        if self.rect.bottom >= TINGGI - 50:
            self.rect.bottom = TINGGI - 50
            self.vel_y = 0
            self.on_ground = True

class Enemy(GameSprite):
    def __init__(self, img, x, y, w, h):
        super().__init__(img, x, y, w, h)

    def update(self):
        self.rect.x -= 6
        if self.rect.x < -50:
            self.rect.x = 800

player = Player('player.png', 100, 200, 50, 50)
enemy1 = Enemy('enemy.png', 600, 400, 50, 50)
enemy2 = Enemy('enemy2.png', 600, 400, 50, 50)

list_enemy = [enemy1, enemy2]
chooseEn = choice(list_enemy)

#FPS
clock = time.Clock()
FPS = 60

stop = False

# Loop Game
run = True
while run:
   clock.tick(FPS)

   # Mendeteksi Event
   for e in event.get():
       if e.type == QUIT:
           run = False
   # Meletakkan Aset dan Objek
   if stop == False:
       window.blit(bg, (0, 0))
       if chooseEn.rect.x < -40:
           chooseEn = choice(list_enemy)
           chooseEn.rect.x = 800
       player.reset()
       player.update()
       chooseEn.reset()
       chooseEn.update()
   display.update()
