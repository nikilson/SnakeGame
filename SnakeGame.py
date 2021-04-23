import pygame
from random import randint
from math import sqrt

pygame.init()
screen_x = 600
screen_y = 600
vel = 1
score = 0
lentail = 0
xtail = []
ytail  = []
status = "up"
live = "run"
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("Snake Game")
snake =  0
x = 20
y = 20
def xyvel():
	global status
	if status =="up":
		x = 0
		y = 30
	elif status =="down":
		x = 0
		y = -30
	elif status == "right":
		x = 30
		y = 0
	elif status == "left":
		x = -30
		y = 0
	return x, y
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
def tailMov():
	global xtail, ytail, lentail, x, y
	if lentail > 0:
		xtemp = xtail[0]
		ytemp = ytail[0]
		xtail[0] = x
		ytail[0] = y
		if lentail > 1:
			for i in range(1, lentail):
				xnext = xtail[i]
				ynext = ytail[i]
				xtail[i] = xtemp
				ytail[i] = ytemp
				xtemp = xnext
				ytemp = ynext
		for tl in range(0, lentail):
			pygame.draw.rect(screen, "yellow", ((xtail[tl]*30)-29, (ytail[tl]*30)-29, 29, 29))
def collision():
	global xf, yf, x, y, xtail, ytail, lentail
	if (xf == x) and (yf == y):
		xf, yf = randnums()
		lentail += 1
		xvel, yvel = xyvel()
		if lentail > 1:
			xtmp = xtail[-1]+xvel
			ytmp = ytail[-1]+yvel 
			xtail.append(xtmp)
			ytail.append(ytmp)
		else:
			xtail.append(x+xvel)
			ytail.append(y+yvel)
def main():
	global keys, status, live, x, y
	if keys[pygame.K_LEFT] and x>0:
		status = "left" 
	if keys[pygame.K_RIGHT] and x<numYlines:
		status = "right"
	if keys[pygame.K_UP]:
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
    clock.tick(20)
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ScreenStatus = False
    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))
    drawLines()
    food()
    main()
    collision()
    tailMov()
    pygame.display.update()