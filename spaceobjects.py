import pygame
import math
import random

class Base_image():
    def __init__(self, image, x = 0, y = 0, v_x = 0, v_y = 0, angle = 0, angle_speed = 0):
        self.image = pygame.image.load(image).convert_alpha()
        self.display_image = self.image
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.angle = angle
        self.angle_speed = angle_speed
        self.position = [x, y]
        
    def draw(self, screen):
        screen.blit(self.display_image, self.position)
        
        
class Ship(Base_image):
    def __init__(self, image, image_alt, x, y):
        self.image_alt = pygame.image.load(image_alt).convert_alpha()
        self.acc = 0
        self.moving = False
        Base_image.__init__(self, image, x, y)
        #self.display_image = self.image
        
    def set_angle_speed(self, value):
        self.angle_speed = value
        
    def set_acc(self, value):
        self.acc = value
        
    def switch_state(self, value):
        self.moving = value
        
    def update(self):
        self.angle += self.angle_speed
        self.v_x = self.acc * math.cos(math.radians(self.angle))
        self.v_y = self.acc * math.sin(math.radians(self.angle))
        self.x += self.v_x
        self.y -= self.v_y
        
        # baisiai nepatinka bagroundo matmenys uzhardkodint :/
        
        if 0 > self.x or self.x > 800:
            self.x = self.x % 800
        if 0 > self.y or self.y > 600:
                self.y = self.y % 600 
        self.position = [self.x, self.y]
                
        if not self.moving and self.acc > 0:
            self.acc -= 1.5/60
        elif self.acc < 0:
            self.acc = 0
        
        # galima ir geriau
        if not self.moving:
            self.display_image = pygame.transform.rotozoom(self.image, self.angle, 1)
        else:
            self.display_image = pygame.transform.rotozoom(self.image_alt, self.angle, 1)
            
        self.ship_center = self.display_image.get_rect().center
        
        self.position = [self.x - self.ship_center[0], self.y - self.ship_center[1]]
        
        #print (self.position, self.ship_center, self.v_x, self.v_y, self.moving)
        
        
class Asteroid (Base_image):
    def __init__(self, image):
        x = random.randrange(0, 800)
        y = random.randrange(0, 600)
        v_x = random.random()*10 - 5
        v_y = random.random()*10 - 5
        angle = random.randrange(0, 360)
        angle_speed = random.randrange(-10, 10)
        Base_image.__init__(self, image, x, y, v_x, v_y, angle, angle_speed)
        
    def update(self):
        
        self.angle += self.angle_speed
        self.x += self.v_x
        self.y -= self.v_y        


        if 0 > self.x or self.x > 800:
            self.x = self.x % 800
        if 0 > self.y or self.y > 600:
                self.y = self.y % 600      

        #print(self.angle, self.angle_speed)        
                
        self.display_image = pygame.transform.rotozoom(self.image, self.angle, 1)        
        self.aster_center = self.display_image.get_rect().center
        self.position = [self.x - self.aster_center[0], self.y - self.aster_center[1]]