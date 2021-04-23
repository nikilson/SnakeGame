import pygame
from random import randint
from math import sqrt

pygame.init()
screen_x = 600
screen_y = 600
vel = 1
status = "up"
live = "run"
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Snake Game")
snake =  0
x = 20
y = 20
numXlines = screen_x // 30
numYlines = screen_y // 30
def randnums():
	xrand = randint(1, numXlines-1)
	yrand = randint(1, numYlines-1)
	return xrand, yrand
xf, yf = randnums()
def food(screen = screen):
	global xf, yf
	pygame.draw.rect(screen, "red", ((xf*30)-29, (yf*30)-29, 29, 29))
def drawLines():
	global screen, screen_x, screen_y
	numXlines = screen_x // 30
	numYlines = screen_y // 30
	#screen_x = numXlines * 30
	#screen_y = numYlines * 30
	for xl in range(numYlines):
		pygame.draw.line(screen, "white", ( 0, xl*30), (screen_x, xl*30))
	for yl in range(numXlines):
		pygame.draw.line(screen, "white", ( yl*30, 0), (yl*30, screen_y))
def main():
	global keys, status, live, x, y
	if keys[pygame.K_LEFT] and x>0:
		status = "left" 
	if keys[pygame.K_RIGHT] and x<numYlines:
		status = "right"
	if keys[pygame.K_UP] and y<numXlines:
		status = "up"
	if keys[pygame.K_DOWN] and y > 0: 
		status = "down"
	if keys[pygame.K_SPACE]:
		if live == "stop":
			live = "run"
		else:
			live = "stop"
	if status == "up" and live == "run":
		if y < 1:
			y = numYlines+1
		y -= vel
	if status == "down" and live == "run":
		if y > numYlines:
			y = 0
		y += vel
	if status == "left" and live == "run":
		if x < 1:
			x = numXlines+1
		x -= vel
	if status == "right" and live == "run":
		if x > numYlines:
			x = 0
		x += vel
	pygame.draw.rect(screen, "yellow", ((x*30)-29, (y*30)-29, 29, 29))
ScreenStatus = True
while ScreenStatus:
    #pygame.time.get_ticks()
    clock = pygame.time.Clock()
    clock.tick(40)
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ScreenStatus = False
    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))
    drawLines()
    food()
    main()
    pygame.display.update()