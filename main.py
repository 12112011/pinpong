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
platform1 = Picture('platform.png', 420, 200, 30, 100)
platform2 = Picture('platform.png', 50, 200, 30, 100)

start_x = 5
start_y = 5
count = 9

move_r1 = False
move_l1 = False

move_r2 = False
move_l2 = False

d_x = 3
d_y = -3

while not game_over:
    ball.fill()
    platform1.fill()
    platform2.fill()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_r1 = True
            if event.key == pygame.K_LEFT:
                move_l1 = True

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         move_r1 = True
        #     if event.key == pygame.K_LEFT:
        #         move_l1 = True

        elif event.type == pygame.K_1:
            if event.key == pygame.K_w:
                move_r2 = True
            if event.key == pygame.K_s:
                move_l2 = True

        # elif event.type == pygame.K_2:
        #     if event.K == pygame.K_w:
        #         move_r2 = False
        #     if event.K == pygame.K_s:
        #         move_l2 = False




    ball.rect.x += d_x
    ball.rect.y += d_y
    
    if ball.rect.colliderect(platform1.rect):
        d_y *= -1

    if ball.rect.colliderect(platform2.rect):
        d_y *= -1

    if ball.rect.y <= 0:
        d_y *= -1

    if ball.rect.x >= 450:
        d_x *= -1

    if ball.rect.x <= 0:
        d_x *= -1

    if ball.rect.y >= 450:
        d_y *= -1


    if move_r1:
        platform1.rect.y += 10
        if platform1.rect.y > 10:
            move_r1 = False
    if move_l1:
        platform1.rect.y -= 10
        if platform1.rect.y > 10:
            move_l1 = False

    if move_r2:
        platform2.rect.y += 10
        if platform2.rect.y > 10:
            move_l2 = False
    if move_l2:
        platform2.rect.y -= 10
        if platform2.rect.y > 10:
            move_l2 = False


    # if move_r2:
    #     platform2.rect.y += 3
    # if move_l2:
    #     platform2.rect.x -= 3


    platform1.draw()
    platform2.draw()
    ball.draw()

    pygame.display.update()

    clock.tick(40)
