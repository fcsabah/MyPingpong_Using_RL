from pingpong import player1
from pingpong import player2
from pingpong import Ball
from pingpong import func

# def update():
# 	for episode in range(5):
# 		## to do something

# 	print("game over")

if __name__ == "__main__":
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print ("Game Exited by User!")
				pygame.quit()
				quit()

		func()
