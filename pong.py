from turtle import circle
import pygame, sys

def ball_movement():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
    
pygame.init()

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong_Shlong")
clock = pygame.time.Clock()

#Game Shapes

ball = pygame.Rect(screen_width/2-5, screen_height/2-5, 10, 10)
player = pygame.Rect(screen_width - 50, screen_height / 2 - 70 ,10,140)
opponent = pygame.Rect(50, screen_height / 2 - 70 ,10,140)


bg_color = pygame.Color("black")
light_grey = (200,200,200)
ball_color = pygame.Color("yellow")

ball_speed_x = 5
ball_speed_y = 5
player_speed = 0
while True:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 5
            if event.key == pygame.K_UP:
                player_speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 5
            if event.key == pygame.K_UP:
                player_speed += 5
        
    ball_movement()
    player.y += player_speed

    if player.top <= 0:
        player.top  = 0;
    if player.bottom >= screen_height:
        player.bottom = screen_height
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,ball_color,ball)
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))

    pygame.display.flip()
    clock.tick(120)#80 frames per second