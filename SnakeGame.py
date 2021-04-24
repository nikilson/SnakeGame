import pygame
from random import randint
#from math import sqrt

pygame.init()
screen_x = 600
screen_y = 600
bgimg = pygame.image.load('back.jpg')
bgimg = pygame.transform.scale(bgimg, (screen_x ,screen_y))
font = pygame.font.Font('freesansbold.ttf', 32)
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
x = 15
y = 15
def showText():
    global screen, score
    showScore = font.render("Score : " + str(score), True, 'white')
    #showSpeed = font.render("Speed : " + speedinkm, True, '#FFE77AFF')
    screen.blit(showScore, (10, 10))
    #screen.blit(showSpeed, (10, 50))
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
def addatail():
	global xtail, ytail, x, y, lentail
	lentail += 1
	if lentail > 1:
		xvel, yvel = xyvel()
		xtmp = xtail[-1]+xvel
		ytmp = ytail[-1]+yvel 
		xtail.append(xtmp)
		ytail.append(ytmp)
	else:
		xvel, yvel = xyvel()
		xtail.append(x+xvel)
		ytail.append(y+yvel)
addatail()
addatail()
numXlines = screen_x // 30
numYlines = screen_y // 30
def randnums():
	xrand = randint(3, numXlines-1)
	yrand = randint(3, numYlines-1)
	return xrand, yrand
xf, yf = randnums()
def food(screen = screen):
	global xf, yf
	pygame.draw.rect(screen, "red", ((xf*30)-30, (yf*30)-30, 30, 30))
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
	if live == "run":
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
		#print(xtail, ytail)
	for tl in range(0, lentail):
		pygame.draw.rect(screen, "yellow", ((xtail[tl]*30)-30, (ytail[tl]*30)-30, 30, 30))
def collision():
	global xf, yf, x, y, xtail, ytail, lentail, score
	if (xf == x) and (yf == y):
		xf, yf = randnums()
		addatail()
		score += 10
def checklive():
	global x, y, xtail, ytail, lentail, live
	for l in range(1, lentail):
		if (x==xtail[l]) and (y==ytail[l]):
			live = "stop"
		else:
			pass
	#print(xtail, ytail)
def main():
	global keys, status, live, x, y
	if keys[pygame.K_LEFT] and status != "right":
		status = "left" 
	if keys[pygame.K_RIGHT] and status != "left":
		status = "right"
	if keys[pygame.K_UP] and status != "down":
		status = "up"
	if keys[pygame.K_DOWN] and status != "up": 
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
clock = pygame.time.Clock()
while ScreenStatus:
    #pygame.time.get_ticks()
    pygame.time.delay(50)
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ScreenStatus = False
    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))
    screen.blit(bgimg, (0, 0))
    #drawLines()
    showText()
    food()
    main()
    collision()
    tailMov()
    checklive()
    pygame.display.update()