import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type, "bird")
        self.rect.y = 270
