from pygame import *

font.init()
mixer.init()

window = display.set_mode((1100, 700))
display.set_caption('Ping Pong')

fon = transform.scale(image.load('fon.jpg'), (1100, 700))


class Gamesprite(sprite.Sprite):
    def __init__(self, img, speed, x, y, sizeX, sizeY):
        super().__init__()
        self.image = transform.scale(image.load(img), (sizeX, sizeY))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(Gamesprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500:
            self.rect.y += self.speed

    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

Player_1 = Player('raketka.jpg', 7, 10, 300, 30, 200)
Player_2 = Player('raketka.jpg', 7, 1060, 300, 30, 200)

Myachik = Gamesprite('Myachik.png', 8, 450, 250, 150, 105)


game = True
finish = True
clock = time.Clock()
while game:

    if finish:
        window.blit(fon, (0, 0))
        Player_1.update()
        Player_2.update_2()
        Player_1.reset()
        Player_2.reset()
        Myachik.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)