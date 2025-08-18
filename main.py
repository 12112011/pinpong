import pygame

pygame.init()

back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

racket_x = 200
racket_y = 330

game_over = False


class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', racket_x, racket_y, 100, 30)

start_x = 5
start_y = 5
count = 9
monsters = list()
for j in range(3):
    y = start_y + (55 * j)
    x = start_x + (27.5 * j)  # и 27.5 по x
    count = count - 1

move_r = False
move_l = False

d_x = 3
d_y = -3

while not game_over:
    ball.fill()
    platform.fill()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_r = True
            if event.key == pygame.K_LEFT:
                move_l = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_r = False
            if event.key == pygame.K_LEFT:
                move_l = False


    for m in monsters:
        m.draw()

    ball.rect.x += d_x
    ball.rect.y += d_y
    
    if ball.rect.colliderect(platform.rect):
        d_y *= -1

    if ball.rect.y <= 0:
        d_y *= -1

    if ball.rect.x >= 450:
        d_x *= -1

    if ball.rect.x <= 0:
        d_x *= -1

    if ball.rect.y >= 500:
        game_over = True  

    if move_r:
        platform.rect.x += 3

    if move_l:
        platform.rect.x -= 3

    platform.draw()
    ball.draw()

    pygame.display.update()

    clock.tick(40)
