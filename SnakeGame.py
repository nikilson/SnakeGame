def main():
	import pygame
	from random import randint
	#from math import sqrt
	from time import sleep
	pygame.init()
	global lentail, status, xtail, ytail, x, y, screen_x, screen_y, screen, score
	global apple, xf, yf, keys, live
	screen_x = 600
	screen_y = 600
	bgimg = pygame.image.load('back.jpg')
	bgimg = pygame.transform.scale(bgimg, (screen_x ,screen_y))
	apple = pygame.image.load('apple.png')
	apple = pygame.transform.scale(apple, (30 ,30))
	font = pygame.font.Font('freesansbold.ttf', 32)
	font1 = pygame.font.Font('freesansbold.ttf', 50)
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
	def eyes():
		global screen, y, x, status
		radius = 3
		xcent = (x * 30) -15
		ycent = (y * 30) -15
		if status == "up":
			ycent = ycent -8
			point1 = (xcent-4, ycent)
			point2 = (xcent+4, ycent)
		elif status == "down":
			ycent = ycent +8
			point1 = (xcent-4, ycent)
			point2 = (xcent+4, ycent)
		elif status == "right":
			xcent = xcent +8
			point1 = (xcent, ycent-4)
			point2 = (xcent, ycent+4)
		elif status == "left":
			xcent = xcent -8
			point1 = (xcent, ycent+4)
			point2 = (xcent, ycent-4)
		pygame.draw.circle(screen, (0,0,0), point1, radius)
		pygame.draw.circle(screen, (0,0,0), point2, radius)
	def showText(pos = (10, 10)):
	    global screen, score, showScore
	    showScore = font.render("Score : " + str(score), True, 'white')
	    #showSpeed = font.render("Speed : " + speedinkm, True, '#FFE77AFF')
	    screen.blit(showScore, pos)
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
		global xf, yf, apple, lentail, xtail, ytail
		for l in range(1, lentail):
			if (xf==xtail[l]) and (yf==ytail[l]):
				xf, yf = randnums()
		#pygame.draw.rect(screen, "red", ((xf*30)-30, (yf*30)-30, 30, 30))
		screen.blit(apple, ((xf*30)-30, (yf*30)-30))
	def drawLines():
		global screen, screen_x, screen_y
		numXlines = screen_x // 30
		numYlines = screen_y // 30
		#screen_x = numXlines * 30
		#screen_y = numYlines * 30
		for xl in range(numYlines):
			pygame.draw.line(screen, "green", ( 0, xl*30), (screen_x, xl*30))
		for yl in range(numXlines):
			pygame.draw.line(screen, "green", ( yl*30, 0), (yl*30, screen_y))
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
		for tl in range(1, lentail):
			pygame.draw.rect(screen, "yellow", ((xtail[tl]*30)-29, (ytail[tl]*30)-29, 29, 29))
	def collision():
		global xf, yf, x, y, xtail, ytail, lentail, score
		if (xf == x) and (yf == y):
			xf, yf = randnums()
			addatail()
			score += 10
	def checklive():
		global x, y, xtail, ytail, lentail, live, vel
		for l in range(1, lentail):
			if (x==xtail[l]) and (y==ytail[l]):
				live = "stop"
				showText(((screen_x//4), (screen_y //2)-30))
				showover = font1.render("Game Over!" + str(score), True, 'red')
				screen.blit(showover, ((screen_x//4)-30, (screen_y //2)+30))
				vel = 0
				#sleep(20)
				#quit()
			else:
				pass
		#print(xtail, ytail)
	def maingame():
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
			if y < 2:
				y = numYlines+1
			y -= vel
		if status == "down" and live == "run":
			if y > numYlines-1:
				y = 0
			y += vel
		if status == "left" and live == "run":
			if x < 2:
				x = numXlines+1
			x -= vel
		if status == "right" and live == "run":
			if x > numYlines-1:
				x = 0
			x += vel
		pygame.draw.rect(screen, "orange", ((x*30)-29, (y*30)-29, 29, 29))
	ScreenStatus = True
	clock = pygame.time.Clock()
	while ScreenStatus:
	    #pygame.time.get_ticks()
	    #delay = 100 - int(score * 0.1)
	    ticktime = 4 + int(score * 0.015)
	    pygame.time.delay(10)
	    clock.tick(ticktime)
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            ScreenStatus = False
	    keys = pygame.key.get_pressed()
	    screen.fill((0, 0, 0))
	    screen.blit(bgimg, (0, 0))
	    #drawLines()
	    showText()
	    eyes()
	    food()
	    maingame()
	    collision()
	    tailMov()
	    checklive()
	    pygame.display.update()
if __name__ == '__main__':
	main()