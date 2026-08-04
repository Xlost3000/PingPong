from pygame import *

font.init()
mixer.init()

window = display.set_mode((1100, 700))
display.set_caption('Ping Pong')

fon = transform.scale(image.load('fon.jpg'), (1100, 700))


game = True
finish = True
clock = time.Clock()
while game:

    if finish:
        window.blit(fon, (0, 0))


    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick()