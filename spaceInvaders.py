# Space Invaders
import pygame
import sys
import time
import random
import threading
#Initialization
pygame.init()

width = 700
height = 700
score = 0
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
flag = 0
ship_width = 40
ship_height = 30


# Colours 
background = (4, 5, 9)
white = (244, 246, 247)
yellow = (241, 196, 15)
orange = (186, 74, 0)
green = (75, 185, 100)
dark_gray = (63, 62, 52)


class score:
    def __init__(self):
       self.score = 0
    def updateScore(self):
        self.score += 1
    def getScore(self):
	return self.score


s = score()


class SpaceShip:
    def __init__(self, x, y, w, h, colour):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colour = colour

    def draw(self):
        pygame.draw.rect(display, yellow, (self.x + self.w/2 - 8, self.y - 10, 16, 10))
	pygame.draw.rect(display, dark_gray, (self.x, self.y, self.w, self.h))

#parent_missile class
class Missile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = 10
    def draw(self): pass
    def move(self): pass
    def hit(self,x,y,d): pass



# Bullet_space Class
class Bullet1(Missile):
    def __init__(self, x, y):
        self.speed = -5
	Missile.__init__(self,x,y)
    def draw(self):
        pygame.draw.ellipse(display, orange, (self.x, self.y, self.d, self.d))

    def move(self):
        self.y += self.speed

    def hit(self, x, y, d):
        if x < self.x < x + d:
            if y + d > self.y > y:
	        s.updateScore()
	        return True



#  Bullet_S Class 
class Bullet2(Missile):
    def __init__(self, x, y):
        self.speed = -10
	Missile.__init__(self,x,y)

    def draw(self):
        pygame.draw.ellipse(display, white, (self.x, self.y, self.d, self.d))

    def move(self):
        self.y += (self.speed)*2

    def hit(self, x, y, d):
        if x < self.x < x + d:
            if y + d > self.y > y:
	        s.updateScore()
		return True


# Alien Class
class Alien:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    def draw1(self):
        pygame.draw.ellipse(display, green, (self.x + self.y/2 - 4, self.y - 6, 16, 10) )
	
    def draw2(self):
        pygame.draw.ellipse(display, yellow, (self.x + self.y/2 - 4, self.y - 6, 16, 10) )


    def shift_down(self):
        self.y += self.d



#The Game 
def game():
    invasion = False
    ship = SpaceShip(width/2-ship_width/2, height-ship_height - 10, ship_width, ship_height, white)

    bullets1 = []
    bullets2 = []
    num_bullet1 = 0
    num_bullet2=0
    for i in range(num_bullet1):
        i = Bullet1(width/2 - 5, height - ship_height - 20)
        bullets1.append(i) 
    for i in range(num_bullet2):
        i = Bullet1(width/2 - 5, height - ship_height - 20)
        bullets2.append(i)


    x_move = 0
    flag = True 
    try:
        while not invasion: 
            if flag == True:
	        aliens = []
                num_aliens = 1
                d = 50
	        i=0	
	        i = Alien(random.randint(1,660),random.randint(15,60), d)
                aliens.append(i)
                #invasion = True 
	    flag = False
	

    #while not invasion:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
		    if event.key == pygame.K_q:
		        pygame.quit()

                    if event.key == pygame.K_d:
                        x_move = 5

                    if event.key == pygame.K_a:
                        x_move = -5

                    if event.key == pygame.K_SPACE:
                        num_bullet1 += 1
                        i = Bullet1(ship.x + ship_width/2 - 5, ship.y)
                        bullets1.append(i)
		
		    if event.key == pygame.K_s:
                        num_bullet2 += 1
                        i = Bullet2(ship.x + ship_width/2 - 5, ship.y)
                        bullets2.append(i)


                if event.type == pygame.KEYUP:
                    x_move = 0

            display.fill(background)

            for i in range(num_bullet1):
                bullets1[i].draw()
                bullets1[i].move()
	
	    for i in range(num_bullet2):
                bullets2[i].draw()
                bullets2[i].move()

            for alien in list(aliens):
                alien.draw1()
		print (alien.x, alien.y, alien.d)
                for item in list(bullets1):
	            #print (alien.x,alien.y,alien.d)
		    
                    if item.hit(alien.x, alien.y, alien.d):
                        bullets1.remove(item)
                        num_bullet1 -= 1
	            	#print (alien.x,alien.y,alien.d, "shot")
			
                        aliens.remove(alien)
                        num_aliens -= 1
                        flag = True
	    
	        for item in list(bullets2):
                    if item.hit(alien.x, alien.y, alien.d):
                        #bullets2.remove(item)
                        #num_bullet2 -= 1
	            	#print (alien.x,alien.y,alien.d, "shot")
			alien.draw2()
                        #aliens.remove(alien)
                        #num_aliens -= 1
			flag = True
			
            ship.x += x_move
            if ship.x < 0:
                ship.x -= x_move
            if ship.x + ship_width > width:
                ship.x -= x_move

            ship.draw()
	    val = s.getScore()
    	    font = pygame.font.SysFont("Wide Latin", 22)
    	    score_var = font.render("Score: " + str(val), True, white)
    	    display.blit(score_var,(300,300))
            pygame.display.update()
            clock.tick(60)
	    #flag = True
    except:
        print "Except"
game()
