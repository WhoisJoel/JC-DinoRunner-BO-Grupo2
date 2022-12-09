from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, CLOUD
from pygame.sprite import Sprite
import random
class Clouds(Sprite):
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint (800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.widht = self.image.get_width()

    def update(self, game):
        self.x -= game.game_speed
        if self.x < -self.widht:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))