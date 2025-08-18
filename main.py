from pygame import *

window = display.set_mode((1100, 820))
window.fill((255, 255, 255))



game = True
while game:
    list_event = event.get()
    window.fill((255, 255, 255))
    for even in list_event:
        if even.type == QUIT:
            game = False

    display.update()
    time.Clock().tick(120)