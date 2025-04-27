from pygame import *
import random

init()

w, h = 800, 600
screen = display.set_mode((w, h))
display.set_caption("Pong")

p_w, p_h = 15, 100
b_size = 30

background = image.load("back.png").convert()
background = transform.scale(background, (w, h))
paddle_img = image.load("platform.png").convert_alpha()
paddle_img = transform.scale(paddle_img, (p_w, p_h))
ball_img = image.load("ball.png").convert_alpha()
ball_img = transform.scale(ball_img, (b_size, b_size))

player = Rect(50, h//2 - p_h//2, p_w, p_h)
opponent = Rect(w - 50 - p_w, h//2 - p_h//2, p_w, p_h)
ball = Rect(w//2 - b_size//2, h//2 - b_size//2, b_size, b_size)

p_speed = 0
o_speed = 0
b_speed_x = 7 * random.choice((1, -1))
b_speed_y = 7 * random.choice((1, -1))

p_score = 0
o_score = 0
try:
    game_font = font.SysFont("Arial", 36)
except:
    game_font = font.Font(None, 36)  # Fallback если Arial не найден

clock = time.Clock()

running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False
        
        if ev.type == KEYDOWN:
            if ev.key == K_s:
                p_speed = 7
            if ev.key == K_w:
                p_speed = -7
            if ev.key == K_DOWN:
                o_speed = 7
            if ev.key == K_UP:
                o_speed = -7
        
        if ev.type == KEYUP:
            if ev.key == K_s or ev.key == K_w:
                p_speed = 0
            if ev.key == K_DOWN or ev.key == K_UP:
                o_speed = 0
    
    screen.blit(background, (0, 0))
    
    player.y += p_speed
    opponent.y += o_speed
    ball.x += b_speed_x
    ball.y += b_speed_y
    
    if player.top <= 0:
        player.top = 0
    if player.bottom >= h:
        player.bottom = h
    
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= h:
        opponent.bottom = h
    
    if ball.top <= 0 or ball.bottom >= h:
        b_speed_y *= -1
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        b_speed_x *= -1
    
    if ball.left <= 0:
        o_score += 1
        ball.center = (w//2, h//2)
        b_speed_x = 7 * random.choice((1, -1))
        b_speed_y = 7 * random.choice((1, -1))
    
    if ball.right >= w:
        p_score += 1
        ball.center = (w//2, h//2)
        b_speed_x = 7 * random.choice((1, -1))
        b_speed_y = 7 * random.choice((1, -1))
    
    screen.blit(paddle_img, player)
    screen.blit(paddle_img, opponent)
    screen.blit(ball_img, ball)
    
    p_text = game_font.render(f"{p_score}", True, (0, 0, 0))
    o_text = game_font.render(f"{o_score}", True, (0, 0, 0))
    screen.blit(p_text, (w//4, 20))
    screen.blit(o_text, (3*w//4, 20))
    
    display.flip()
    clock.tick(60)

quit()