import random
from dino_runner.components.obstacles.obstacles import Obstacle

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__ (image, self.type)
        self.rect.y = random.randint(50,250)
        self.fly = 0

    def draw(self, screen):
        if self.fly >= 9:
            self.fly = 0
        screen.blit(self.image[self.fly//5], self.rect)
        self.fly += 1
        