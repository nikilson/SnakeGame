import SnakeGame
def mainmenu():
	import pygame
	from playsound import playsound
	global screen_x, screen_y, bgimg, snk, font, screen, keys, mouse, but1status
	screen_x = 600
	screen_y = 600
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load('music.mp3')
	pygame.mixer.music.set_volume(0.9)
	pygame.mixer.music.play()
	bgimg = pygame.image.load('back.jpg')
	snk =  pygame.image.load('snake.png')
	font = pygame.font.Font('freesansbold.ttf', 32)
	snk = pygame.transform.scale(snk, (250 , 250))
	bgimg = pygame.transform.scale(bgimg, (screen_x ,screen_y))
	screen = pygame.display.set_mode((screen_x,screen_y))
	pygame.display.set_caption("Snake Game")
	but1status = False
	def rectBox(width, height, xpos, ypos):
		global mouse, screen, but1status
		xpos2 = xpos + width
		ypos2 = ypos + height
		button = pygame.Surface((width, height))
		button.fill((255,255,255))
		if ((mouse[0] < xpos2) and (mouse[0] > xpos) and (mouse[1] < ypos2) and (mouse[1] > ypos)):
			button.set_alpha(150)
			but1status = True
			#pygame.draw.rect(screen,(255, 255, 255, 200),(xpos, ypos, width, height))
		else:
			button.set_alpha(100)
			but1status = False
		screen.blit(button, (xpos, ypos))
			#pygame.draw.rect(screen,(255, 155, 255, 100), (xpos, ypos, width, height))
	def text():
		Entergame = font.render("ENTER GAME", True, 'black')
		screen.blit(Entergame, ((screen_x//2)-100, (screen_y//2)+80))
	ScreenStatus = True
	while ScreenStatus:
	    pygame.time.delay(10)
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            ScreenStatus = False
	        if event.type == pygame.MOUSEBUTTONDOWN:
	        	if but1status == True:
	        		SnakeGame.main()
	        		ScreenStatus = False
	    keys = pygame.key.get_pressed()
	    mouse = pygame.mouse.get_pos()
	    screen.fill((0, 0, 0))
	    screen.blit(bgimg, (0, 0))
	    screen.blit(snk, ((screen_x//2)-120, 60))
	    rectBox( width = 250, height = 60, xpos = (screen_x//2-115), ypos = (screen_y//2)+65)
	    text()
	    pygame.display.update()
mainmenu()