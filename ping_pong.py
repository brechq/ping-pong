from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wigth, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wigth, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.y = player_y
        self.rect.x = player_x

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP]and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
fps = 60

raket1 = Player('racket.png', 30, 200, 4, 50, 150)
raket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

speed_x = 3
speed_y = 3

font.init()
font = font.Font(None, 35)
loss1 = font.render('PLAYER 1 LOSE', True, (180, 0, 0))
loss2 = font.render('PLAYER 2 LOSE', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        raket1.update_l()
        raket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(raket1, ball) or sprite.collide_rect(raket2, ball):
            speed_x *=-1
            speed_y *=1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *=-1

        if ball.rect.x < 0:
            finish = True
            window.blit(loss1, (200, 200))
            game_over = True

        if ball.rect.x > win_width - 50:
            finish = True
            window.blit(loss2, (200, 200))
            game_over = True

        raket1.reset()
        raket2.reset()
        ball.reset()

    display.update()
    clock.tick(fps)