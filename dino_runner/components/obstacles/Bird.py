import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self, image):
        self.type = BIRD[0] if self.step_index < 5 else BIRD[1]
        super().__init__(image, self.type)
        self.rect.y = 400
        
        