import pygame

pygame.init()
screenWidth, screenHeight = 640, 480
gameDisplay = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("SURPRISE :D")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (66, 179, 244)

clock = pygame.time.Clock()

class player1():
	def __init__(self):
		self.padWidth, self.padHeight = 8, 64
		self.x, self.y = 0, screenHeight/2
		self.speed = 3
		self.score = 0

	def scoring(self, gameDisplay):
		myfont = pygame.font.SysFont("Comic Sans MS", 20)
		label = myfont.render("Score "+str(self.score), 1, white)
		gameDisplay.blit(label, (50,20))
		if self.score == 10:
			print("Player 1 Wins!")
			exit()

	def movement(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.y -= self.speed
		elif keys[pygame.K_DOWN]:
			self.y += self.speed

		if self.y <= 0:
			self.y = 0
		elif self.y >= screenHeight-64:
			self.y = screenHeight-64

	def draw(self):
		pygame.draw.rect(gameDisplay, white, (self.x,self.y,self.padWidth,self.padHeight))

class player2():
	def __init__(self):
		self.padWidth, self.padHeight = 8, 64
		self.x, self.y = screenWidth - self.padWidth, screenHeight/2
		self.speed = 3
		self.score = 0

	def scoring(self, gameDisplay):
		myfont = pygame.font.SysFont("Comic Sans MS", 20)
		label = myfont.render("Score "+str(self.score), 1, white)
		gameDisplay.blit(label, (470, 20))
		if self.score == 10:
			print("Player 2 Wins!")
			exit()

	def movement(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.y -= self.speed
		elif keys[pygame.K_s]:
			self.y += self.speed

		if self.y <= 0:
			self.y = 0
		elif self.y >= screenHeight-64:
			self.y = screenHeight-64

	def draw(self):
		pygame.draw.rect(gameDisplay, white, (self.x,self.y,self.padWidth,self.padHeight))    	

class Ball():
	def __init__(self):
		self.ballWidth, self.ballHeight = 8, 8
		self.x, self.y = screenWidth/2, screenHeight/2
		self.speed_x = 3
		self.speed_y = 3

	def movement(self):
		self.x += self.speed_x
		self.y += self.speed_y

		if self.y <= 0:
			self.speed_y *= -1
		elif self.y >= screenHeight - self.ballHeight:
			self.speed_y  *= -1

		if self.x <= 0:
			self.__init__()
			p2.score += 1
		elif self.x >= screenWidth-self.ballWidth:
			self.__init__()
			self.speed_x = 3
			p1.score += 1

		for n in range(-self.ballHeight, p1.padHeight):
			if self.y == p1.y + n:
				if self.x <= p1.x + p1.padWidth:
					self.speed_x *= -1
					break

			n += 1

		for n in range(-self.ballHeight, p2.padHeight):
			if self.y == p2.y + n:
				if self.x >= p2.x - p2.padWidth:
					self.speed_x *= -1
					break

			n += 1

	def draw(self):
		pygame.draw.rect(gameDisplay, white, (self.x,self.y,self.ballWidth,self.ballHeight))


p1 = player1()
p2 = player2()
ball = Ball()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print ("Game Exited by User!")
			pygame.quit()
			quit()

	p1.movement()
	p2.movement()
	ball.movement()


	gameDisplay.fill((black))

	p1.draw()
	p2.draw()
	ball.draw()
	p1.scoring(gameDisplay)
	p2.scoring(gameDisplay)

	pygame.display.flip()
	clock.tick(60)


