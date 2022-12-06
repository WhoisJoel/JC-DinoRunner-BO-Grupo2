import pygame
import math

from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, DEFAULT_TYPE, DUCKING, JUMPING

class Dinosaurius(Sprite):
    X_POS = 80
    Y_POS = 300
    JUMP_VEL = 8
    def __init__(self):
        self.dino_run = {DEFAULT_TYPE: RUNNING}
        self.dino_duck = {DEFAULT_TYPE: DUCKING}
        self.dino_jump = {DEFAULT_TYPE: JUMPING}

        self.image = self.dino_run[DEFAULT_TYPE][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.steps = 0
        self.jump_vel = self.JUMP_VEL
        self.running = True
        self.ducking = False
        self.jumping = False
    
    def update(self, input_user):
        if self.running:
            self.run()
        
        if self.ducking:
            self.duck()
        
        if self.jumping:
            self.jump()
        
        if input_user[pygame.K_DOWN] and not self.jumping:
            self.ducking = True
            self.running = False
            self.jumping = False
        elif input_user[pygame.K_UP] and not self.jumping:
            self.jumping = True
            self.running = False
            self.ducking = False
        elif not (self.jumping or input_user[pygame.K_DOWN]):
            self.running = True
            self.ducking = False
            self.jumping = False
    
        if self.steps >= 10:
            self.steps = 0

    def run(self):
        self.image = self.dino_run[DEFAULT_TYPE][0] if self.steps <=5 else self.dino_run[DEFAULT_TYPE][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.steps += 1

    def duck(self):
        self.image = self.dino_duck[DEFAULT_TYPE][0] if self.steps <=5 else self.dino_duck[DEFAULT_TYPE][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS + 35
        self.steps += 1

    def jump(self):
        self.image = self.dino_jump[self.type]
        self.image = JUMPING
        if self.jumping:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
            
        
        
            

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


    
